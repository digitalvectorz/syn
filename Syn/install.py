"""
Simple install routines 

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Install a binball to the filesystem
"""

import Syn.exceptions
import Syn.policy.db as D
import Syn.package_registry

def maskedExtract(fullpkgpath, dbinf):
	"""
	Extract shit directly
	"""
	ROOT_PATH = D.DB_ROOT
	fullpkgpath = D.DB_ROOT + fullpkgpath
	Interferometric = Syn.common.getcwd()
	Syn.sh.cd(D.DB_ROOT)

	Syn.sh.ensuredir(fullpkgpath)
	Syn.sh.cd(fullpkgpath)

	dbinf.extractall()
	Syn.sh.cd(Interferometric)


def install(synball):
	"""
	Install installs a synball to the syn staging area, making sure to
	carefully note the status of the package in the pkgdb.
	@arg synball: Syn tarball to install.
	"""
	ROOT_PATH = D.DB_ROOT
	pkgdb  = Syn.package_registry.package_registry(ROOT_PATH)
	cruldb = Syn.package_registry.crul_registry(ROOT_PATH)

	try:
		dbinf = Syn.binary_tarball.binary_tarball(synball)
		package = dbinf.get_metablob()
		Syn.log.l(Syn.log.VERBOSE,"Package is name: %s" % package['package'])
		fullpkgpath = "/" + package['package'][0] + "/" + package['package']

		Syn.log.l(Syn.log.VERBOSE,"Package path is: %s" % fullpkgpath)

		try:
			pkgid = cruldb.getPackage(package['package'])
			Syn.log.l(Syn.log.PEDANTIC,"Package DB Dump: %s" % pkgid)
			Syn.log.l(Syn.log.VERBOSE,"Going to have to compare versions and upgrade...")
			# Migrate version upgrade
		except Syn.exceptions.PackageNotFoundException as e:
			Syn.log.l(Syn.log.VERBOSE,"New package install!")
			# Direct extraction, klobber.
			cruldb.setPackage(package['package'], "HALF-INSTALLED")
			maskedExtract(fullpkgpath, dbinf)
			cruldb.setPackage(package['package'], "INSTALLED")
			pkgdb.setPackage(package['package'], dbinf.packageize())
			pkgdb.write()
			cruldb.write()

	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

