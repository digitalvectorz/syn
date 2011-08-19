"""
Useful Package abstractions

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Package abstractions
"""

import Syn.Policy.PackageRegistry as R
import Syn.Policy.Universal        as U
import Syn.Exceptions

class PackageAttrs:
	"""
	Package attribute object stuff. This stores
	the following data in a sane way:

	 * Package Name
	 * Version
	 * Syn Local Version
	 * Dependencies
	"""
	def __init__(self, package, version, vlocal, deps):
		"""
		Basic constructor.
		@param package: name of the package
		@param version: version of the package
		@param vlocal:  Syn-local version number
		@param deps:    package dependencies
		"""
		self._pkg    = package
		self._ver    = version
		self._vlocal = vlocal
		self._dep    = deps

	def val(self):
		"""
		Validate the package attrs. No clue why this is
		called `val`. Don't blame me, plox.
		"""
		try:
			x = self._pkg
			y = self._ver
			z = self._dep
			a = self._vlocal

			if x != "" and y != "" and a != "" and type(z) == list:
				return True
		except ValueError as e:
			pass
		return False

	def format(self):
		"""
		Create a format-dict out of the package attrs.
		@return: a dict with the given dict attrs intact.
		"""
		if not self.val():
			raise Syn.Exceptions.SynFormatException("The fuck is this?")
		ret = {
			R.NAME_ATTR : self._pkg,
			R.VERS_ATTR : self._ver,
			R.DEPS_ATTR : self._dep,
			R.LOCL_ATTR : self._vlocal
		}
		return ret
class package:
	"""
	Package class, we use this to abstract all sorts
	of package data when doing dependency stuff.
	"""
	def __init__(self, attrs):
		"""
		Simple constructor
		@param attrs: format-dict of attrs.
		"""
		if type(attrs) == dict:
			attrs = PackageAttrs(
				attrs[R.NAME_ATTR],
				attrs[R.VERS_ATTR],
				attrs[R.LOCL_ATTR],
				attrs[R.DEPS_ATTR]
			)
		if attrs.val() == False:
			raise Syn.Exceptions.SynFormatException("The fuck is this?")
		self.pkgattr = attrs

	def val(self):
		"""
		Validate the package. Again, no clue why this is called `val`.
		"""
		return self.pkgattr.val()

	def getDeps(self):
		"""
		Get the package's dependencies in a sane clear way.
		@return: a list of the package's deps
		"""
		return self.pkgattr.format()[R.DEPS_ATTR]

	def getStatus(self):
		"""
		Get a package's install status. Fuck does this work?
		XXX: Intensive code review of this method needed. CRULL call needed?
		@return installed status.
		"""
		return self.pkgattr.format()[R.STAT_ATTR]

	def getName(self):
		"""
		Get the package's name
		@return: the name of the goddamn package.
		"""
		return self.pkgattr.format()[R.NAME_ATTR]

	def format(self):
		"""
		Return the attr's format dict, simple composed passthrough
		@return: a formated dict
		"""
		return self.pkgattr.format()

