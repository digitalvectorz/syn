# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber
import Syn.exceptions
import Syn.policy.db as D
import Syn.package_registry

PLUMBING_NAME = "install-package"
PREFIX = ""

def run(args):
	ROOT_PATH = PREFIX + D.DB_ROOT
	if not Syn.sh.xists(ROOT_PATH):
		Syn.sh.mkdir(ROOT_PATH)
	pkgdb = Syn.package_registry.package_registry(ROOT_PATH)

	try:
		try:
			dbinf = pkgdb.getPackage(args[2])
		except Syn.exceptions.SynException as e:
			Syn.log.l(Syn.log.VERBOSE,"New install for %s" % args[2])
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

Syn.plumber.registerRoute(PLUMBING_NAME, run)

