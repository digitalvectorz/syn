# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.source_package as S
import Syn.source_tarball
import Syn.exceptions
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

	destdir = cwd + "/" + S.STAGE_DIR
	Syn.common.putenv(S.DESTDIR, destdir)

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

	print runStage("cfg")
	print runStage("build")
	print runStage("stage")

