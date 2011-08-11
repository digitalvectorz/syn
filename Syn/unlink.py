"""
Simple unlink routines 

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 8th, 2011, 00:10 -0000

 Unlink a package into the filesystem
"""

import os.path
import Syn.exceptions
import Syn.policy.db as D
import Syn.policy.binary_package as B
import Syn.policy.chroot as C
import Syn.package_registry

def unlink(packageid):
	"""
	Unlink a package from filesystem, and get ready
	to do some awesomeness.

	@arg packageid: Name of the package to unlink into the filesystem.
	"""
	ROOT_PATH = D.DB_ROOT
	pkgdb  = Syn.package_registry.package_registry(ROOT_PATH)
	cruldb = Syn.package_registry.crul_registry(ROOT_PATH)

	try:
		pkgid  = cruldb.getPackage(packageid)
		pkginf =  pkgdb.getPackage(packageid).format()
		Syn.log.l(Syn.log.PEDANTIC,"Package DB Dump: %s" % pkgid)
		package_root = pkgid['path']
		popdir = Syn.common.getcwd()
		Syn.sh.cd(ROOT_PATH + package_root)
		Syn.sh.cd("./" + B.FS_ROOT)

		tree = Syn.common.getDirectoryTree()

		supercool = {}

		for t in tree:
			supercool[t[1:]] = os.path.abspath(t)

		crul = cruldb.getPackage(packageid)
		crul_status = crul['status']
		crul_path   = crul['path']

		if crul_status != "LINKED":
			raise Syn.exceptions.PackageNotinstalledException("Package not linked! -- " + packageid)
		else:
			Syn.log.l(Syn.log.PEDANTIC,"Package linked. unlinking.")

		cruldb.setPackage(packageid, {
			"status" : "HALF-LINKED",
			"path"   : crul_path
		})
		cruldb.write()

		for s in supercool:
			Syn.log.l(Syn.log.PEDANTIC,"Removing: %s" % s)
			Syn.sh.rm(C.CHROOT + s)

		cruldb.setPackage(packageid, {
			"status" : "INSTALLED",
			"path"   : crul_path
		})
		cruldb.write()


		Syn.sh.cd(popdir)
	except Syn.exceptions.PackageNotFoundException as e:
		Syn.log.l(Syn.log.VERBOSE,"Shit. No package found. Passing exception up")
		raise e
