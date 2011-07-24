# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.package_registry as R
import Syn.policy.universal        as U

class package_attrs:
	def __init__(self, package, version, vlocal, deps, status):
		self._pkg    = package
		self._ver    = version
		self._vlocal = vlocal
		self._dep    = deps
		self._status = status

	def val(self):
		try:
			x = self._pkg
			y = self._ver
			z = self._dep
			a = self._vlocal
			b = self._status

			if b in R.STATUS_VALUE and x != "" and y != "" and a != "" and type(z) == list:
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
			R.DEPS_ATTR : self._dep,
			R.LOCL_ATTR : self._vlocal,
			R.STAT_ATTR : self._status
		}
		return ret
class package:
	def __init__(self, attrs):
		if type(attrs) == dict:
			attrs = package_attrs(
				attrs[R.NAME_ATTR],
				attrs[R.VERS_ATTR],
				attrs[R.LOCL_ATTR],
				attrs[R.DEPS_ATTR],
				attrs[R.STAT_ATTR]
			)
		if attrs.val() == False:
			raise Syn.exceptions.SynFormatException("The fuck is this?")
		self.pkgattr = attrs
	def val(self):
		return self.pkgattr.val()
	def getDeps(self):
		return self.pkgattr.format()[R.DEPS_ATTR]
	def getStatus(self):
		return self.pkgattr.format()[R.STAT_ATTR]
	def format(self):
		return self.pkgattr.format()

