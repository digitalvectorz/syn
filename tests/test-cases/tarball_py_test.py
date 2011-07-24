#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import unittest
import Syn.tarball
import os.path
class TarBallTestCase(unittest.TestCase):
	def setUp(self):
		test_tarball = "test-0.1.tar.gz"
		self.tar = Syn.tarball.tarball(test_tarball)
	def testGetRoot(self):
		test_root = "test-0.1"
		assert test_root==self.tar.getRootFolder(),'couldnt get root folder'
	def testOSExist(self):
		test_root = "test-0.1"
		assert os.path.exists(test_root) == False,'test_root exists'
		self.tar.extractall()
		assert os.path.exists(test_root) == True,'test_root not extracted'

def suite():
	tarballTestSuite=unittest.TestSuite()
	tarballTestSuite.addTest(TarBallTestCase("setUp"))
	tarballTestSuite.addTest(TarBallTestCase("testGetRoot"))
	tarballTestSuite.addTest(TarBallTestCase("testOSExist"))
	return tarballTestSuite

test=suite()
result=unittest.TestResult()
test.run(result)

assert result.wasSuccessful()==True

