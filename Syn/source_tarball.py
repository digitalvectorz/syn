# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.log
import tarfile

import Syn.tarball
import Syn.policy.source_package as S

class source_tarball(Syn.tarball.tarball):
	def verify(self):
		root_bullshit = self.getRootFolder()
		assert_exists = []
		for x in S.SOURCE_DIR_REQ_FILES:
			assert_exists.append(root_bullshit + "/" + S.SOURCE_DIRECTORY + "/" + x)
		for y in assert_exists:
			fd = self.readMember(y)
			crap = fd.read()
			if crap != "":
				Syn.log.l(Syn.log.PEDANTIC,"Exists: %s" % y)
