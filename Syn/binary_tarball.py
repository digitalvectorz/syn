"""
binary_tarball, a simple binary tarball module.
"""
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.log
import Syn.tarball
import Syn.exceptions
import Syn.policy.binary_package as B
import Syn.md5sum

import os.path
import tarfile

class binary_tarball(Syn.tarball.tarball):
	"""
	This class provides clean access to a syn compiled 
	binary tarball. It's interface matches very closely with a
	`source_tarball`, and provides similar functionality.
	"""
	def verify(self):
		"""
		Verify that the binary tarball is in good working shape,
		and has all the required files needed to consider it a
		valid binary tarball. Checksum shazbits should be checked
		as well. This is automagically called by the constructor.
		"""
		assert_exists = []

		for x in B.BINARY_DIR_REQ_FILES:
			assert_exists.append(x)

		for y in assert_exists:
			try:
				fd = self.readMember(y)
				crap = fd.read()
				if crap != "":
					Syn.log.l(Syn.log.PEDANTIC,"Exists: %s" % y)
					
			except KeyError as e:
				raise Syn.exceptions.SynFormatException("Bad binary tarball (missing: %s)" % y)
		
		if not Syn.md5sum.md5sumfilematches("meta/filesums", self.md5()): # checksum failed
			Syn.log.l(Syn.log.CRITICAL,"Checksum: Failed!")
		else:
			Syn.log.l(Syn.log.VERBOSE,"Checksum: Passed!")

	def upstream_tarball_id(self):
		"""
		`upstream_tarball_id` yanks the tarball name from the wget
		string, so that we can see what the tarball's name should
		be. This can be krufty in a binary_tarball.
		@return: A String which contains the upstream .tarball's name.
		"""
		figgleforth = self.get_metablob()
		return os.path.basename(figgleforth["wget-url"])

	def package_fullid(self):
		"""
		`package_fullid` snags the package's full package identifier,
		in the format of package-n.m, where n.m is the release number,
		and package is the name of the package. If the package was
		"Bash", and the version was "4.2" the full ID would be:
		"bash-4.2". This is used for file strings etc.
		@return: The package's full String ID.
		"""
		figgleforth = self.get_metablob()
		return os.path.basename(figgleforth["package"] + "-" + figgleforth["version"])

	def get_metablob(self):
		"""
		`get_metablob` digests the tarball and loads the JSON manifest
		so that we can play with it. `package_fullid` and
		`upstream_tarball_id` use this to get the dict.
		@return: A dict with the key/values in the manifest.
		"""
		targs = Syn.common.getTempLocation()

		Syn.log.l(Syn.log.VERBOSE,"Using temp loc: %s" % targs)

		self.tarball_target.extract(
			B.META_ROOT + "/" + B.METAFILE,
			targs
		)

		sbf = Syn.json_bfile.json_bfile(
			targs + "/" + B.META_ROOT + "/" + B.METAFILE
		)
		figgleforth = sbf.getContent()

		Syn.sh.rmdir(targs)
		return figgleforth
