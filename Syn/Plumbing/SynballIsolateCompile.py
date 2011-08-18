# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Policy.SourcePackage as S
import Syn.SourceTarball
import Syn.Exceptions
import Syn.Plumber
import Syn.Common
import Syn.Sh

PLUMBING_NAME = "synball-isolate-compile"

def run(args):
	"""
	Move all sources to a temp location and build there. This helps
	protect the CWD from dammage during a test build
	"""
	try:
		if not Syn.Sh.xists(args[2]):
			raise KeyError('offset 2')

		cwd = Syn.Common.getcwd()

		wd = Syn.Common.getTempLocation()
		if Syn.Sh.xists(wd):
			raise Syn.Exceptions.ConflictException("Fuck all, dir exists: %s" % wd)

		stb = Syn.SourceTarball.SourceTarball(args[2])
		fullid   = stb.getPackageFullId()
		upstream = stb.getUpstreamTarballId()

		needed_filez = [
			fullid + S.XTN,
			upstream
		]

		Syn.Sh.mkdir(wd)
		for x in needed_filez:
			Syn.Sh.cp(x, wd)

		Syn.Sh.cd(wd)

		binary = Syn.Synd.build(fullid + S.XTN)

		Syn.Sh.cd(cwd)
		Syn.Sh.mv(binary, cwd)
		Syn.Sh.rmdir(wd)
	except KeyError as e:
		raise Syn.Exceptions.FileNotPresentException("Fucking asshole. No file: %s" % e)
Syn.Plumber.registerRoute(PLUMBING_NAME, run)

