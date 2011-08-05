# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

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

class package_registry():
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
			pkg_data = working_db[package]
			ret = Syn.package.package(pkg_data)
			return ret
		except KeyError as e:
			raise Syn.exceptions.PackageNotFoundException("No such package: %s" % package)

class crul_registry():
	def __init__(self, path=None):
		if path == None:
			path = U.SLASH_TOP_LEVEL_DIR
		path = path + "/" + R.CRULBASE_FILE
		self.__loaddb(path)
	def __loaddb(self, path):
		try:
			self.ff = flatfile.json_bfile(path)
		except IOError as e:
			l.l(l.CRITICAL,"Database does not exist.")
			raise Syn.exceptions.SynDirectoryFailure("%s does not exist." % path)

