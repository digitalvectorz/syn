#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.source_tarball
import Syn.exceptions
<<<<<<< HEAD

stb = Syn.source_tarball.source_tarball("test-1.0.syn.tar.gz")

try:
	stb2 = Syn.source_tarball.source_tarball("test-1.0-bad.syn.tar.gz")
	assert True == False
except Syn.exceptions.SynFormatException as e:
	print "Failed with glee"
=======
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
>>>>>>> 1c78a129958db3d97e5d8ad353ae571286e6b8ad
