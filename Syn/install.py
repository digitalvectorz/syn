# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.exceptions
import Syn.policy.db as D
import Syn.package_registry

def install(synball):
	ROOT_PATH = D.DB_ROOT
	pkgdb = Syn.package_registry.package_registry(ROOT_PATH)

	try:
		dbinf = Syn.binary_tarball.binary_tarball(synball)
		package = dbinf.get_metablob()
		Syn.log.l(Syn.log.VERBOSE,"Package is name: %s" % package['package'])
		fullpkgpath = "/" + package['package'][0] + "/" + package['package']

		Syn.log.l(Syn.log.VERBOSE,"Package path is: %s" % fullpkgpath)

		try:
			pkgid = pkgdb.getPackage(package['package'])
			Syn.log.l(Syn.log.PEDANTIC,"Package DB Dump: %s" % pkgid)
			# Migrate version upgrade
		except Syn.exceptions.PackageNotFoundException as e:
			Syn.log.l(Syn.log.VERBOSE,"New package install!")
			# Direct extraction, klobber.

	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

