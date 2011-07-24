#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import Syn.tarball
import os.path
import delt as d
import unittest

class md5TestCase(unittest.TestCase):
	def compareTest(self): 
		test_tarball = "md5test.tar.gz"
		test_root    = "md5test"

		t = Syn.tarball.tarball(test_tarball)
		root = t.getRootFolder()

		test_dict = {
			'md5test/bar':'5bf487da0233682aa1b52bccbc530ab8',
			'md5test/baz':'86cdc6230a4b73b4aa606f27d178979e',
			'md5test/foo':'26bb73556ceb32a5df30b733c5355ee5'
		}


		assert d.delt(t.md5(), test_dict) == {}

	
def suite():
	md5TestSuite = unittest.TestSuite()
	md5TestSuite.addTest(md5TestCase("compareTest"))
	return md5TestSuite

testSuite=suite()
result=unittest.TestResult()
testSuite.run(result)

assert result.wasSuccessful()
