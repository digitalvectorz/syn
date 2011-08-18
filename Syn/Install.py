"""
Simple install routines 

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Install a binball to the filesystem
"""

import Syn.Exceptions
import Syn.Policy.Db as D
import Syn.PackageRegistry

def maskedExtract(fullpkgpath, dbinf):
	"""
	Extract shit directly
	"""
	ROOT_PATH = D.DB_ROOT
	fullpkgpath = D.DB_ROOT + fullpkgpath
	Interferometric = Syn.Common.getcwd()
	Syn.Sh.cd(D.DB_ROOT)

	Syn.Sh.ensuredir(fullpkgpath)
	Syn.Sh.cd(fullpkgpath)

	dbinf.extractall()
	Syn.Sh.cd(Interferometric)

def doInstall(pkgdb, cruldb, fullpkgpath, dbinf, package):
	"""
	Do the m'fn' install
	XXX: Document me
	@warning: this may fuck stuff up seriously if used directly.
	"""
	cruldb.setPackage(package['package'], {
		"status" : "HALF-INSTALLED",
		"path" : fullpkgpath
	})
	maskedExtract(fullpkgpath, dbinf)
	cruldb.setPackage(package['package'], {
		"status" : "INSTALLED",
		"path" : fullpkgpath
	})
	pkgdb.setPackage(package['package'], dbinf.packageize())
	pkgdb.write()
	cruldb.write()

def install(synball):
	"""
	Install installs a synball to the syn staging area, making sure to
	carefully note the status of the package in the pkgdb.
	@arg synball: Syn.Tarball to install.
	"""
	ROOT_PATH = D.DB_ROOT
	pkgdb  = Syn.PackageRegistry.PackageRegistry(ROOT_PATH)
	cruldb = Syn.PackageRegistry.CrulRegistry(ROOT_PATH)

	try:
		dbinf = Syn.BinaryTarball.BinaryTarball(synball)
		package = dbinf.getMetablob()
		Syn.Log.l(Syn.Log.VERBOSE,"Package is name: %s" % package['package'])
		fullpkgpath = "/" + package['package'][0] + "/" + package['package'] + "/" + package['version'] + "/" + str(package['local-version'])

		Syn.Log.l(Syn.Log.VERBOSE,"Package path is: %s" % fullpkgpath)

		try:
			pkgid  = cruldb.getPackage(package['package'])
			pkginf =  pkgdb.getPackage(package['package']).format()
			Syn.Log.l(Syn.Log.PEDANTIC,"Package DB Dump: %s" % pkgid)
			# Do conflict catching etc
			doInstall(pkgdb, cruldb, fullpkgpath, dbinf, package)
		except Syn.Exceptions.PackageNotFoundException as e:
			Syn.Log.l(Syn.Log.VERBOSE,"New package install!")
			# Frack yeah.
			doInstall(pkgdb, cruldb, fullpkgpath, dbinf, package)

	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

