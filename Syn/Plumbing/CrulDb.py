# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Policy.Db as D

import Syn.PackageRegistry
import Syn.Plumber
import Syn.Sh

PLUMBING_NAME = "query-crul-db"

# Need to add in reset-able roots

PREFIX = ""

def run(args):
	"""
	Dump everything we know about a package
	"""
	ROOT_PATH = PREFIX + D.DB_ROOT
	if not Syn.Sh.xists(ROOT_PATH):
		Syn.Sh.mkdir(ROOT_PATH)
	pkgdb = Syn.PackageRegistry.CrulRegistry(ROOT_PATH)
	try:
		print pkgdb.getPackage(args[2])
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))
	except Syn.Exceptions.PackageNotFoundException as e:
		raise Syn.Exceptions.PackageNotinstalledException("No such package: %s" % e)

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

