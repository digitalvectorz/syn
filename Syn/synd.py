# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.source_package as S
import Syn.policy.binary_package as B
import Syn.policy.metafile as M
import Syn.binary_tarball
import Syn.source_tarball
import Syn.exceptions
import Syn.json_bfile
import Syn.json_file
import Syn.tarball
import Syn.common
import Syn.log
import os.path
import tarfile
import Syn.sh
import os

def deslash(foo):
	"""
	De-slash a directory name
	"""
	if foo[-1:] == "/":
		return deslash(foo[:-1])
	return foo

def runStage(Stage, syndRoot = "./"):
	"""
	runStage allows you to run a "build" file target
	(Stage) on the CWD, from any root (syndRoot).
	"""
	bldfile = syndRoot + S.SOURCE_DIRECTORY + "/" + S.BUILDFILE
	[ status, output ] = Syn.common.run("./" + bldfile + " " + Stage)
	Syn.log.l(Syn.log.PEDANTIC,"Stage: %s finished with status %s" % (Stage, status))
	return output

def packageSynd():
	"""
	packageSynd tars and compresses the synd for
	use as a builder. There is only a mild ammount of sanity
	checking in the source_tarball class that ensures this is OK.
	"""
	wdir = Syn.common.getcwd()
	package = os.path.basename(wdir)
	Syn.log.l(Syn.log.PEDANTIC,"Found package top-level as: %s" % package)
	FPATH = package + S.XTN
	Syn.sh.cd("..")
	tarball = tarfile.open(FPATH, 'w:gz')
	tarball.add(package)
	tarball.close()
	mf = Syn.json_file.json_file(S.SOURCE_DIRECTORY + "/" + S.METAFILE)
	dickt = mf.getContent()
	pkg = dickt['package']
	ver = dickt['version']
	fullpath="%s-%s" % (pkg, ver)
	ret = Syn.source_tarball.source_tarball(FPATH)
	Syn.sh.cd(package)
	return ret

def loadEnv():
	"""
	This loads the build.env json_file into the current env, so we can
	spawn build targets with the right ENV-vars in place.
	"""
	envfile = S.SOURCE_DIRECTORY + "/" + S.ENVFILE
	pkginfo = S.SOURCE_DIRECTORY + "/" + S.METAFILE

	env  = Syn.json_file.json_file(envfile)
	crap = Syn.json_file.json_file(pkginfo)

	envdict  = env.getContent()
	crapdict = crap.getContent()

	cwd = Syn.common.getcwd()
	Syn.log.l(Syn.log.PEDANTIC, "ENV CWD: " + cwd)

	destdir    = cwd + "/" + S.STAGE_ROOT + "/" + S.STAGE_FOLD
	binaryRoot = cwd + "/" + S.STAGE_ROOT

	Syn.common.putenv(S.DESTDIR,     destdir)
	Syn.common.putenv(S.BINARY_ROOT, binaryRoot)

	# print crapdict

	pkg = crapdict['package']
	ver = crapdict['version']

	Syn.common.putenv(S.PACKAGE, pkg)
	Syn.common.putenv(S.VERSION, ver)

	for x in S.BUILD_ENV_KEYS:
		try:
			val = envdict[x]
		except KeyError as e:
			Syn.log.l(Syn.log.CRITICAL,"Oh shit. Env key missing: %s" % e)
			raise Syn.exceptions.SynFormatException(str(e))

		if type(val) == list:
			combined_val = ""
			for y in envdict[x]:
				combined_val += y + " "
			Syn.common.putenv(x, combined_val)
		else:
			Syn.common.putenv(x, val)

def migrateMetadata():
	"""
	This migrates the Synd plain-jane json_file into a shortened
	binary json_bfile with tags stripped out. This is called to create
	the binary metafile at the end of the build process.

	Please note this needs to have the ENV set up, this uses the ENV to
	find where to put the binary file. Don't be stupid :)
	"""
	# Note, this *NEEDS* the envsetup before use.
	metadir = Syn.common.getenv(S.BINARY_ROOT)
	metadir = metadir + "/" + S.STAGE_META

	Syn.log.l(Syn.log.PEDANTIC,"Metastage: %s" % metadir)

	if not Syn.sh.xists(metadir):
		Syn.sh.mkdir(metadir)

	metafile = S.SOURCE_DIRECTORY + "/" + S.METAFILE
	meta = Syn.json_file.json_file(metafile)
	metadickt = meta.getContent()
	binaryBlob = {}

	for k in M.META_BINARY_MIGRATE:
		try:
			binaryBlob[k] = metadickt[k]
		except KeyError as e:
			Syn.log.l(Syn.log.CRITICAL,"XXX: FIXME Missing migration tag: %s!!!" % k)

	bblob = Syn.json_bfile.json_bfile(metadir + "/" + B.METAFILE)
	bblob.setContent(binaryBlob)
	bblob.write()

def packageBuiltBinaryFolder():
	"""
	This packages the binary DESTDIR folders (root and metadata)
	into a tarball, and returns it as a binary_package.

	Note: This needs to have the env set up from the build,
	this uses the env gto get the build directory. Don't be stupid :)
	"""
	# Note, this *NEEDS* the envsetup before use.
	broot = Syn.common.getenv(S.BINARY_ROOT)
	metadir = Syn.common.getenv(S.DESTDIR)

	popdir = Syn.common.getcwd()
	Syn.sh.cd(broot) # n-cwd - ./bash-4.1/ 

	bblob = Syn.json_bfile.json_bfile(broot + "/" + S.STAGE_META + "/" + B.METAFILE)
	packagedata = bblob.getContent()
	fullid = "%s-%s" % ( packagedata["package"], packagedata["version"] )
	tarball = tarfile.open(fullid + B.XTN, 'w:gz')
	tarball.add(S.STAGE_META)
	tarball.add(S.STAGE_FOLD)
	tarball.close()
	synball = Syn.binary_tarball.binary_tarball(fullid + B.XTN)

	Syn.sh.cd(popdir)
	return synball

def build(synball):
	"""
	Clean entry point to do a full-on build of a syn tarball. This
	does it in place. Be ready to make a mess of the CWD
	"""
	src = Syn.source_tarball.source_tarball(synball)
	rf = src.getRootFolder()
	# test if directory exists and fail.
	Syn.log.l(Syn.log.PEDANTIC,"Loading tarball %s with root %s" % (synball, rf))
	src.extractall()

	upstream_tarball = src.upstream_tarball_id()

	tb = Syn.tarball.tarball(upstream_tarball)
	rf_us = tb.getRootFolder()
	rf_us = deslash(rf_us)
	if rf_us != rf:
		Syn.log.l(Syn.log.CRITICAL,"Fuck, upstream root directory and synd root are not the same. ABORT!")
		Syn.log.l(Syn.log.CRITICAL," Expected: %s" % rf)
		Syn.log.l(Syn.log.CRITICAL,"      Got: %s" % rf_us)
		raise Syn.exceptions.SynFormatException("Fuck'n syn directory does not match")

	tb.extractall()
	Syn.sh.cd(rf)
	loadEnv()

	print runStage("cfg") # XXX: Add in logging and stuff
	print runStage("build")
	print runStage("stage")

	migrateMetadata()
	syn = packageBuiltBinaryFolder()

	tarball = S.STAGE_ROOT + "/" + src.package_fullid() + B.XTN
	Syn.sh.mv(tarball, "../" + src.package_fullid() + B.XTN)

	return os.path.abspath("../" + src.package_fullid() + B.XTN)
