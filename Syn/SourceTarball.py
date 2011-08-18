"""
Useful source-package abstractions

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Package abstractions
"""

import json
import Syn.Log
import Syn.Tarball
import Syn.Exceptions
import Syn.Policy.SourcePackage as S

import os.path
import tarfile

class SourceTarball(Syn.Tarball.Tarball):
	"""
	Source tarball R/U stuff. We're extending
	`Syn.Tarball.Tarball`.
	"""
	def verify(self):
		"""
		Verify that a tarball is clean. We'll run `Syn.Synlint` against
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
					Syn.Log.l(Syn.Log.PEDANTIC,"Exists: %s" % y)
			except KeyError as e:
				raise Syn.Exceptions.SynFormatException("Bad source tarball")

	def getUpstreamTarballId(self):
		"""
		Get the upstream tarball's name. We pull this from
		`wget-url` in the metafile.
		@return: Tarball name.
		"""
		figgleforth = self.getMetablob()
		return os.path.basename(figgleforth["wget-url"])

	def getPackageFullId(self):
		"""
		Get the package's "Syn-name" (in the format of
		fluxbox-1.3.1).
		@return: the package's syn-name.
		"""
		figgleforth = self.getMetablob()
		return os.path.basename(figgleforth["package"] + "-" + figgleforth["version"])

	def packageize(self):
		"""
		package-ize a Syn.Tarball into a package object, for use in the pool
		or other resolution type tasks.
		@return a `Syn.PackageRegistry.package_attrs` object
		"""
		shit = self.getMetablob()
		bpatr = Syn.PackageRegistry.package_attrs(
			shit['package'], shit['version'], shit['syn-policy-version'], shit['deps'])
		return bpatr

	def getMetablob(self):
		"""
		Super fancy script to get the metafile's content for use.
		Most calls that report meta-data (`getPackageFullId` etc)
		are wrapped calls and filters on this.
		@return: super cool metafile dict.
		"""
		m = self.readMember(self.getRootFolder() + "/" + S.SOURCE_DIRECTORY + "/" + S.METAFILE)
		metafile = m.read()
		figgleforth = json.loads(metafile)
		return figgleforth
