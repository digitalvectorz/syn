# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.log
import Syn.tarball
import Syn.exceptions
import Syn.policy.binary_package as B

import os.path
import tarfile

class binary_tarball(Syn.tarball.tarball):
	def verify(self):
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

