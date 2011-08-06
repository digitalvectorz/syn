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
	if path == None:
		path = U.SLASH_TOP_LEVEL_DIR
	db_path = path + "/" + R.DATABASE_FILE
	lu_path = path + "/" + R.CRULBASE_FILE

	ffdb = flatfile.json_bfile(db_path)
	ludb = flatfile.json_bfile(lu_path)
	ffdb.blankFile()
	ludb.blankFile()

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

	def write(self):
		self.ff.write()

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
	def setPackage(self, package, status):
		if not status in R.STATUS_VALUE:
			raise Syn.exceptions.SynUnknownStatusException("Fuck all. Unknown status: %s" % status)
		ShortID = R.STATUS_VALUE[status]
		cpay = self.ff.getContent()
		cpay[package] = status

	def write(self):
		self.ff.write()

	def getPackage(self, package):
		try:
			cpay = self.ff.getContent()
			return cpay[package]
		except KeyError as e:
			raise Syn.exceptions.PackageNotFoundException(e)
