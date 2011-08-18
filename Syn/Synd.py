"""
Syn directory goodies

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Syn directory shaz
"""

import Syn.Policy.SourcePackage as S
import Syn.Policy.BinaryPackage as B
import Syn.Policy.Metafile as M
import Syn.Policy.Build as BP
import Syn.BinaryTarball
import Syn.SourceTarball
import Syn.Exceptions
import Syn.JsonBfile
import Syn.JsonFile
import Syn.Tarball
import Syn.Common
import Syn.Log
import os.path
import tarfile
import Syn.Sh
import os
import Syn.Md5sum

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
	try:
		[ status, output ] = Syn.Common.run("./" + bldfile + " " + Stage)
	except KeyboardInterrupt as e:
		return (-1024, "User terminated stage with control-c.")
	Syn.Log.l(Syn.Log.PEDANTIC,"Stage: %s finished with status %s" % (Stage, status))
	return (status, output)

def packageSynd():
	"""
	packageSynd tars and compresses the synd for
	use as a builder. There is only a mild ammount of sanity
	checking in the.SourceTarball class that ensures this is OK.
	"""
	mf = Syn.JsonFile.JsonFile(S.SOURCE_DIRECTORY + "/" + S.METAFILE)
	dickt = mf.getContent()
	pkg = dickt['package']
	ver = dickt['version']
	fullpath="%s-%s" % (pkg, ver)
	wdir = Syn.Common.getcwd()
	package = os.path.basename(wdir)
	Syn.Log.l(Syn.Log.PEDANTIC,"Found package top-level as: %s" % package)
	FPATH = fullpath + S.XTN
	Syn.Sh.cd("..")
	tarball = tarfile.open(FPATH, 'w:gz')
	tarball.add(package)
	tarball.close()
	ret = Syn.SourceTarball.SourceTarball(FPATH)
	Syn.Sh.cd(package)
	return ret

def loadEnv():
	"""
	This loads the build.env JsonFile into the current env, so we can
	spawn build targets with the right ENV-vars in place.
	"""
	envfile = S.SOURCE_DIRECTORY + "/" + S.ENVFILE
	pkginfo = S.SOURCE_DIRECTORY + "/" + S.METAFILE

	env  = Syn.JsonFile.JsonFile(envfile)
	crap = Syn.JsonFile.JsonFile(pkginfo)

	envdict  = env.getContent()
	crapdict = crap.getContent()

	cwd = Syn.Common.getcwd()
	Syn.Log.l(Syn.Log.PEDANTIC, "ENV CWD: " + cwd)

	destdir    = cwd + "/" + S.STAGE_ROOT + "/" + S.STAGE_FOLD
	binaryRoot = cwd + "/" + S.STAGE_ROOT

	Syn.Common.putenv(S.DESTDIR,     destdir)
	Syn.Common.putenv(S.BINARY_ROOT, binaryRoot)

	# print crapdict

	pkg = crapdict['package']
	ver = crapdict['version']

	Syn.Common.putenv(S.PACKAGE, pkg)
	Syn.Common.putenv(S.VERSION, ver)

	for x in S.BUILD_ENV_KEYS:
		try:
			val = envdict[x]
		except KeyError as e:
			Syn.Log.l(Syn.Log.CRITICAL,"Oh shit. Env key missing: %s" % e)
			raise Syn.Exceptions.SynFormatException(str(e))

		if type(val) == list:
			combined_val = ""
			for y in envdict[x]:
				combined_val += y + " "
			Syn.Common.putenv(x, combined_val)
		else:
			Syn.Common.putenv(x, val)

def migrateMetadata():
	"""
	This migrates the Synd plain-jane JsonFile into a shortened
	binary JsonBfile with tags stripped out. This is called to create
	the binary metafile at the end of the build process.

	Please note this needs to have the ENV set up, this uses the ENV to
	find where to put the binary file. Don't be stupid :)
	"""
	# Note, this *NEEDS* the envsetup before use.
	metadir = Syn.Common.getenv(S.BINARY_ROOT)
	metadir = metadir + "/" + S.STAGE_META

	Syn.Log.l(Syn.Log.PEDANTIC,"Metastage: %s" % metadir)

	if not Syn.Sh.xists(metadir):
		Syn.Sh.mkdir(metadir)

	metafile = S.SOURCE_DIRECTORY + "/" + S.METAFILE
	meta = Syn.JsonFile.JsonFile(metafile)
	metadickt = meta.getContent()
	binaryBlob = {}

	for k in M.META_BINARY_MIGRATE:
		try:
			binaryBlob[k] = metadickt[k]
		except KeyError as e:
			Syn.Log.l(Syn.Log.CRITICAL,"XXX: FIXME Missing migration tag: %s!!!" % k)

	bblob = Syn.JsonBfile.JsonBfile(metadir + "/" + B.METAFILE)
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
	broot = Syn.Common.getenv(S.BINARY_ROOT)
	metadir = Syn.Common.getenv(S.DESTDIR)

	popdir = Syn.Common.getcwd()
	Syn.Sh.cd(broot) # n-cwd - ./bash-4.1/ 

	# checksum bs
	Syn.Md5sum.createMd5HashFile(".", S.STAGE_META + "/" + B.FILESUMS)

	bblob = Syn.JsonBfile.JsonBfile("./" + S.STAGE_META + "/" + B.METAFILE)
	packagedata = bblob.getContent()
	fullid = "%s-%s" % ( packagedata["package"], packagedata["version"] )
	tarball = tarfile.open(fullid + B.XTN, 'w:gz')
	tarball.add(S.STAGE_META)
	tarball.add(S.STAGE_FOLD)
	tarball.close()
	synball = Syn.BinaryTarball.BinaryTarball(fullid + B.XTN)

	Syn.Sh.cd(popdir)
	return synball

def build(synball):
	"""
	Clean entry point to do a full-on build of a syn tarball. This
	does it in place. Be ready to make a mess of the CWD
	"""
	src = Syn.SourceTarball.SourceTarball(synball)
	rf = src.getRootFolder()
	# test if directory exists and fail.
	Syn.Log.l(Syn.Log.PEDANTIC,"Loading tarball %s with root %s" % (synball, rf))
	src.extractall()

	upstream_tarball = src.getUpstreamTarballId()

	tb = Syn.Tarball.Tarball(upstream_tarball)
	rf_us = tb.getRootFolder()
	rf_us = deslash(rf_us)
	if rf_us != rf:
		Syn.Log.l(Syn.Log.CRITICAL,"Fuck, upstream root directory and synd root are not the same. ABORT!")
		Syn.Log.l(Syn.Log.CRITICAL," Expected: %s" % rf)
		Syn.Log.l(Syn.Log.CRITICAL,"      Got: %s" % rf_us)
		raise Syn.Exceptions.SynFormatException("Fuck'n syn directory does not match")

	tb.extractall()
	Syn.Sh.cd(rf)
	loadEnv()

	fd = open(S.STAGE_LOGS, "w")

	for x in BP.BUILD_PROCESS:
		(status, log) = runStage(x) ### XXX: LOGGING, PLEASE
		fd.write("============= Stage =============\n")
		fd.write(" Build Stage: %s\n" % x)
		fd.write("=================================\n")
		fd.write(log)
		if status != 0:
			# Fuckshit. shit shit shit.
			raise Syn.Exceptions.BuildFailureException("Failed on stage %s" % x)

	migrateMetadata()
	syn = packageBuiltBinaryFolder()

	tarball = S.STAGE_ROOT + "/" + src.getPackageFullId() + B.XTN
	Syn.Sh.mv(tarball, "../" + src.getPackageFullId() + B.XTN)

	return os.path.abspath("../" + src.getPackageFullId() + B.XTN)
