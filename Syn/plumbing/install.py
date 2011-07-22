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
		dbinf = Syn.binary_tarball.binary_tarball(args[2])
		Syn.log.l(Syn.log.VERBOSE,"Package is type: %s" % dbinf.package_fullid())
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

Syn.plumber.registerRoute(PLUMBING_NAME, run)

