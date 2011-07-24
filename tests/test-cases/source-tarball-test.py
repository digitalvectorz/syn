#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.source_tarball
import Syn.exceptions
import unittest
class tarballTestCase(unittest.TestCase):
	def sourceTarTest(self):
		stb = Syn.source_tarball.source_tarball("test-1.0.syn.tar.gz")

		try:
			stb2 = Syn.source_tarball.source_tarball("test-1.0-bad.syn.tar.gz")
			assert True == True
		except Syn.exceptions.SynFormatException as e:
			print "Failed with glee"
			assert True == False
def suite():
	tarballTestSuite = unittest.TestSuite()
	tarballTestSuite.addTest(tarballTestCase("sourceTarTest"))
	return tarballTestSuite

testSuite=suite()
result=unittest.TestResult()
testSuite.run(result)


assert result.wasSuccessful()
