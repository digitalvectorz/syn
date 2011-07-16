# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.log
import tarfile

import Syn.tarball
import Syn.policy.source_package as S

class source_tarball(Syn.tarball.tarball):
	def verify(self):
		assert_exists = []
		for x in S.SOURCE_DIR_REQ_FILES:
			assert_exists.append(S.SOURCE_DIRECTORY + "/" + x)
		for y in assert_exists:
			fd = self.readMember(y)
