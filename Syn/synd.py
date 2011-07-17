# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.source_package as S
import Syn.source_tarball
import Syn.exceptions
import Syn.json_file
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
				combined_val += y
			Syn.common.putenv(x, combined_val)
		else:
			Syn.common.putenv(x, val)

