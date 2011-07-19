# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.source_package as S
import Syn.policy.binary_package as B
import Syn.policy.metafile as M
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

def runStage(Stage, syndRoot = "./"):
	bldfile = syndRoot + S.SOURCE_DIRECTORY + "/" + S.BUILDFILE
	[ status, output ] = Syn.common.run("./" + bldfile + " " + Stage)
	Syn.log.l(Syn.log.PEDANTIC,"Stage: %s finished with status %s" % (Stage, status))
	return output

def packageSynd():
	wdir = Syn.common.getcwd()
	package = os.path.basename(wdir)
	Syn.log.l(Syn.log.PEDANTIC,"Found package top-level as: %s" % package)
	FPATH = package + S.XTN
	tarball = tarfile.open(FPATH, 'w')
	Syn.sh.cd("..")
	tarball.add(package)
	tarball.close()
	Syn.sh.cd(package)
	return Syn.source_tarball.source_tarball(FPATH)

def loadEnv():
	envfile = S.SOURCE_DIRECTORY + "/" + S.ENVFILE
	env = Syn.json_file.json_file(envfile)
	envdict = env.getContent()

	cwd = Syn.common.getcwd()
	Syn.log.l(Syn.log.PEDANTIC, "ENV CWD: " + cwd)

	destdir = cwd + "/" + S.STAGE_DIR
	Syn.common.putenv(S.DESTDIR, destdir)

	binaryRoot = cwd + "/" + S.STAGE_ROOT
	Syn.common.putenv(S.BINARY_ROOT, binaryRoot)

	Syn.log.l(Syn.log.PEDANTIC, "Set DESTDIR as %s" % destdir)

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
	# Note, this *NEEDS* the envsetup before use.
	metadir = Syn.common.getenv(S.DESTDIR)
	Syn.log.l(Syn.log.PEDANTIC,"Metadir as: %s" % metadir)
	metadir = metadir + "/" + S.STAGE_META_DIR
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
	# Note, this *NEEDS* the envsetup before use.
	broot = Syn.common.getenv(S.BINARY_ROOT)
	metadir = Syn.common.getenv(S.DESTDIR)

	popdir = Syn.common.getcwd()
	Syn.sh.cd(broot)
	bblob = Syn.json_bfile.json_bfile(broot + "/" + S.STAGE_DIR + "/" + S.STAGE_META_DIR +
		"/" + B.METAFILE)
	packagedata = bblob.getContent()
	fullid = "%s-%s" % ( packagedata["package"], packagedata["version"] )
	tarball = tarfile.open(fullid + B.XTN, 'w')
	tarball.add(S.STAGE_META)
	tarball.add(S.STAGE_FOLD)
	tarball.close()
	synball = Syn.binary_tarball.binary_tarball(fullid + B.XTN)
	return synball


def build(synball):
	src = Syn.source_tarball.source_tarball(synball)
	rf = src.getRootFolder()
	# test if directory exists and fail.
	Syn.log.l(Syn.log.PEDANTIC,"Loading tarball %s with root %s" % (synball, rf))
	src.extractall()

	upstream_tarball = src.upstream_tarball_id()

	tb = Syn.tarball.tarball(upstream_tarball)
	rf_us = tb.getRootFolder()
	if rf_us != rf:
		Syn.log.l(Syn.log.CRITICAL,"Fuck, upstream root directory and synd root are not the same. ABORT!")
		Syn.log.l(Syn.log.CRITICAL," Expected: %s" % rf)
		Syn.log.l(Syn.log.CRITICAL,"      Got: %s" % rf_us)
		raise Syn.exceptions.SynFormatException("Fuck'n syn directory does not match")

	tb.extractall()
	Syn.sh.cd(rf)
	loadEnv()

	#runStage("cfg")
	#runStage("build")
	#runStage("stage")

	migrateMetadata()
	packageBuiltBinaryFolder()
