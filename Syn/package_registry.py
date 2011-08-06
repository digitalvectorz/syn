"""
Useful pickle-type stuff

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Uses a json_bfile to store package info
"""

import Syn.log as l
import Syn.json_bfile as flatfile

import Syn.policy.package_registry as R
import Syn.policy.universal        as U

from Syn.package import package_attrs

import Syn.package

import Syn.exceptions

#
# root
#  +-> package_name
#         +-> version          : 0.0
#         +-> local            : 1
#         +-> deps
#               +-> foo
#               +-> bar
#               +-> baz
#

# Someone fix this to user super-classes.

def do_not_call_me_nukestrap_database_files(path=None):
	"""
	@warning: DO NOT CALL THIS BY HAND
	This is used to blast the .crul and .pkgdb files
	into piss and back. Please don't call it. It will
	really screw up the package's states.
	@arg path: Root path.
	@return: shame and hate.
	"""
	if path == None:
		path = U.SLASH_TOP_LEVEL_DIR
	db_path = path + "/" + R.DATABASE_FILE
	lu_path = path + "/" + R.CRULBASE_FILE

	ffdb = flatfile.json_bfile(db_path)
	ludb = flatfile.json_bfile(lu_path)
	ffdb.blankFile()
	ludb.blankFile()

class package_registry():
	"""
	Package informational database -- contains such things as
	package name, version, local version, and dependencies. Very
	dry and dull.

	XXX: Look into superclassing this to stop the "Seiter-guilt".
	"""
	def __init__(self, path=None):
		"""
		Simple constructor.
		@arg path: root path. useful for chroot work without chroot.
		"""
		if path == None:
			path = U.SLASH_TOP_LEVEL_DIR
		path = path + "/" + R.DATABASE_FILE
		self.__loaddb(path)

	def __loaddb(self, path):
		"""
		Load the database into the cache. Very useful. Called
		by the constructor.
		@arg path: chroot-esque root-shim.
		"""
		try:
			self.ff = flatfile.json_bfile(path)
		except IOError as e:
			l.l(l.CRITICAL,"Database does not exist.")
			raise Syn.exceptions.SynDirectoryFailure("%s does not exist." % path)

	def setPackage(self, package, payload):
		"""
		set the package's information in the database by hand
		usually used with `getPackage`.
		@arg package: name of the package
		@arg payload: package attrs and such.
		"""
		if payload.val():
			cpay = self.ff.getContent()
			cpay[package] = payload.format()

	def write(self):
		"""
		Write out data from the cache to the DB.
		"""
		self.ff.write()

	def getPackage(self, package):
		"""
		Get some package information out of the flatfile DB.
		@arg package: package to check out
		@return: a nice cute little dict of data.
		"""
		working_db = self.ff.getContent()
		try:
			pkg_data = working_db[package]
			ret = Syn.package.package(pkg_data)
			return ret
		except KeyError as e:
			raise Syn.exceptions.PackageNotFoundException("No such package: %s" % package)

class crul_registry():
	"""
	CRUL (Link, Unlink, Remove, Install -- Install has a C in it) database.
	 Jesus. How did I manage to get an acronym that wrong? Someone come up
	 with a better name for me, eh?

	This maintains a package's status in the filesystem.
	"""
	def __init__(self, path=None):
		"""
		Default simple constructor.		
		@arg path: chroot-esque root path to klobber loading.
		"""
		if path == None:
			path = U.SLASH_TOP_LEVEL_DIR
		path = path + "/" + R.CRULBASE_FILE
		self.__loaddb(path)

	def __loaddb(self, path):
		"""
		Load a database into the cache. Called by the
		constructor. 
		"""
		try:
			self.ff = flatfile.json_bfile(path)
		except IOError as e:
			l.l(l.CRITICAL,"Database does not exist.")
			raise Syn.exceptions.SynDirectoryFailure("%s does not exist." % path)

	def setPackage(self, package, status):
		"""
		Set package info in the CRULBase
		@arg package: package name.
		@arg status:  package installed status
		"""
		if not status in R.STATUS_VALUE:
			raise Syn.exceptions.SynUnknownStatusException("Fuck all. Unknown status: %s" % status)
		ShortID = R.STATUS_VALUE[status]
		cpay = self.ff.getContent()
		cpay[package] = status

	def write(self):
		"""
		Write out the database to the filesystem.
		"""
		self.ff.write()

	def getPackage(self, package):
		"""
		Get a package's set of data out of the CRULbase
		This is nice to help check to see what a package
		is up to right now. We'll use this for all
		sorts of good things.
		@arg package: package to lookup
		@return: a dict of goodies
		"""
		try:
			cpay = self.ff.getContent()
			return cpay[package]
		except KeyError as e:
			raise Syn.exceptions.PackageNotFoundException(e)
