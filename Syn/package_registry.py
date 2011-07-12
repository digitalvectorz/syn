# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.log as l
import Syn.json_bfile as flatfile

import Syn.policy.package_registry as R
import Syn.policy.universal        as U

import Syn.exceptions

#
# root
#  +-> package_name
#         +-> installed_status : foo
#         +-> version          : 0.0
#         +-> deps
#               +-> foo
#               +-> bar
#               +-> baz
#

class package_registry:
	def __init__(self, path=None):
		if path == None:
			path = U.SLASH_TOP_LEVEL_DIR
		path = path + "/" + R.DATABASE_FILE
		self.__loaddb(path)

	def __loaddb(self, path):
		try:
			self.ff = flatfile.json_bfile(path)
		except IOError as e:
			l.l(l.CRITICAL,"Database does not exist.")
			raise Syn.exceptions.SynDirectoryFailure("%s does not exist." % path)
	def setPackage(self, package, payload):
		if payload.val():
			cpay = self.ff.getContent()
			cpay[package] = payload.format()

	def getPackage(self, package):
		working_db = self.ff.getContent()
		try:
			return working_db[package]
		except KeyError as e:
			raise Syn.exceptions.PackageNotFoundException("No such package: %s" % package)

class package_attrs:
	def __init__(self, package, version, deps):
		self._pkg = package
		self._ver = version
		self._dep = deps
	def val(self):
		try:
			x = self._pkg
			y = self._ver
			z = self._dep
			if x != "" and y != "" and type(z) == list:
				return True
		except ValueError as e:
			pass

		return False
	def format(self):
		if not self.val():
			raise Syn.exceptions.SynFormatException("The fuck is this?")
		ret = {
			R.NAME_ATTR : self._pkg,
			R.VERS_ATTR : self._ver,
			R.DEPS_ATTR : self._dep
		}
		return ret

