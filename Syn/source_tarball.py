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
	def verify(self):
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
		figgleforth = self.get_metablob()
		return os.path.basename(figgleforth["wget-url"])

	def package_fullid(self):
		figgleforth = self.get_metablob()
		return os.path.basename(figgleforth["package"] + "-" + figgleforth["version"])

	def packageize(self):
		"""
		XXX: Fixme
		"""
		shit = self.get_metablob()
		bpatr = Syn.package_registry.package_attrs(
			shit['package'], shit['version'], shit['local'], shit['deps'])
		return bpatr

	def get_metablob(self):
		m = self.readMember(self.getRootFolder() + "/" + S.SOURCE_DIRECTORY + "/" + S.METAFILE)
		metafile = m.read()
		figgleforth = json.loads(metafile)
		return figgleforth
