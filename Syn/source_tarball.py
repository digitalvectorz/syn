"""
Useful source-package abstractions

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Package abstractions
"""

import json
import Syn.log
import Syn.tarball
import Syn.exceptions
import Syn.policy.source_package as S

import os.path
import tarfile

class source_tarball(Syn.tarball.tarball):
	"""
	Source tarball R/U stuff. We're extending
	`Syn.tarball.tarball`.
	"""
	def verify(self):
		"""
		Verify that a tarball is clean. We'll run `Syn.synlint` against
		it's metafile and a few other tidbits of checking.
		"""
		root_bullshit = self.getRootFolder()
		assert_exists = []
		for x in S.SOURCE_DIR_REQ_FILES:
			assert_exists.append(root_bullshit + "/" + S.SOURCE_DIRECTORY + "/" + x)
		for y in assert_exists:
			try:
				fd = self.readMember(y)
				crap = fd.read()
				if crap != "":
					Syn.log.l(Syn.log.PEDANTIC,"Exists: %s" % y)
			except KeyError as e:
				raise Syn.exceptions.SynFormatException("Bad source tarball")

	def upstream_tarball_id(self):
		"""
		Get the upstream tarball's name. We pull this from
		`wget-url` in the metafile.
		@return: Tarball name.
		"""
		figgleforth = self.get_metablob()
		return os.path.basename(figgleforth["wget-url"])

	def package_fullid(self):
		"""
		Get the package's "Syn-name" (in the format of
		fluxbox-1.3.1).
		@return: the package's syn-name.
		"""
		figgleforth = self.get_metablob()
		return os.path.basename(figgleforth["package"] + "-" + figgleforth["version"])

	def packageize(self):
		"""
		package-ize a Syn-tarball into a package object, for use in the pool
		or other resolution type tasks.
		@return a `Syn.package_registry.package_attrs` object
		"""
		shit = self.get_metablob()
		bpatr = Syn.package_registry.package_attrs(
			shit['package'], shit['version'], shit['syn-policy-version'], shit['deps'])
		return bpatr

	def get_metablob(self):
		"""
		Super fancy script to get the metafile's content for use.
		Most calls that report meta-data (`package_fullid` etc)
		are wrapped calls and filters on this.
		@return: super cool metafile dict.
		"""
		m = self.readMember(self.getRootFolder() + "/" + S.SOURCE_DIRECTORY + "/" + S.METAFILE)
		metafile = m.read()
		figgleforth = json.loads(metafile)
		return figgleforth
