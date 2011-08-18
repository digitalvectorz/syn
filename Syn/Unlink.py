"""
Simple unlink routines 

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 8th, 2011, 00:10 -0000

 Unlink a package into the filesystem
"""

import os.path
import Syn.Exceptions
import Syn.Policy.Db as D
import Syn.Policy.BinaryPackage as B
import Syn.Policy.Chroot as C
import Syn.PackageRegistry

def unlink(packageid):
	"""
	Unlink a package from filesystem, and get ready
	to do some awesomeness.

	@arg packageid: Name of the package to unlink into the filesystem.
	"""
	ROOT_PATH = D.DB_ROOT
	pkgdb  = Syn.PackageRegistry.PackageRegistry(ROOT_PATH)
	cruldb = Syn.PackageRegistry.CrulRegistry(ROOT_PATH)

	try:
		pkgid  = cruldb.getPackage(packageid)
		pkginf =  pkgdb.getPackage(packageid).format()
		Syn.Log.l(Syn.Log.PEDANTIC,"Package DB Dump: %s" % pkgid)
		package_root = pkgid['path']
		popdir = Syn.Common.getcwd()
		Syn.Sh.cd(ROOT_PATH + package_root)
		Syn.Sh.cd("./" + B.FS_ROOT)

		tree = Syn.Common.getDirectoryTree()

		supercool = {}

		for t in tree:
			supercool[t[1:]] = os.path.abspath(t)

		crul = cruldb.getPackage(packageid)
		crul_status = crul['status']
		crul_path   = crul['path']

		if crul_status != "LINKED":
			raise Syn.Exceptions.PackageNotinstalledException("Package not linked! -- " + packageid)
		else:
			Syn.Log.l(Syn.Log.PEDANTIC,"Package linked. unlinking.")

		cruldb.setPackage(packageid, {
			"status" : "HALF-LINKED",
			"path"   : crul_path
		})
		cruldb.write()

		for s in supercool:
			Syn.Log.l(Syn.Log.PEDANTIC,"Removing: %s" % s)
			Syn.Sh.rm(C.CHROOT + s)

		cruldb.setPackage(packageid, {
			"status" : "INSTALLED",
			"path"   : crul_path
		})
		cruldb.write()


		Syn.Sh.cd(popdir)
	except Syn.Exceptions.PackageNotFoundException as e:
		Syn.Log.l(Syn.Log.VERBOSE,"Shit. No package found. Passing exception up")
		raise e
