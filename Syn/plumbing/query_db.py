# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.db as D

import Syn.package_registry
import Syn.plumber
import Syn.sh

PLUMBING_NAME = "query-db"

# Need to add in reset-able roots

PREFIX = ""

def run(args):
	"""
	Dump everything we know about a package
	"""
	ROOT_PATH = PREFIX + D.DB_ROOT
	if not Syn.sh.xists(ROOT_PATH):
		Syn.sh.mkdir(ROOT_PATH)
	pkgdb = Syn.package_registry.package_registry(ROOT_PATH)
	try:
		print pkgdb.getPackage(args[2])
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))
	except Syn.exceptions.PackageNotFoundException as e:
		raise Syn.exceptions.PackageNotinstalledException("No such package: %s" % e)

Syn.plumber.registerRoute(PLUMBING_NAME, run)

