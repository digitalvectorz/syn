"""
Simple link routines 

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 8th, 2011, 00:10 -0000

 Link a package into the filesystem
"""

import Syn.exceptions
import Syn.policy.db as D
import Syn.package_registry

def link(packageid):
	"""
	Link a package into the filesystem, and get ready
	to do some awesomeness.

	@arg packageid: Name of the package to link into the filesystem.
	"""
	ROOT_PATH = D.DB_ROOT
	pkgdb  = Syn.package_registry.package_registry(ROOT_PATH)
	cruldb = Syn.package_registry.crul_registry(ROOT_PATH)

	try:
		pkgid  = cruldb.getPackage(packageid)
		pkginf =  pkgdb.getPackage(packageid).format()
		Syn.log.l(Syn.log.PEDANTIC,"Package DB Dump: %s" % pkgid)
		# Do conflict catching etc

	except Syn.exceptions.PackageNotFoundException as e:
		Syn.log.l(Syn.log.VERBOSE,"Shit. No package found. Passing exception up")
		raise e
