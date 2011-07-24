#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>


import Syn.sh as o
import unittest

class osTestCase(unittest.TestCase):
	def makeTwiceTest(self):
		testdir = "os_test_dir"

		o.mkdir(testdir)

		try:
			o.mkdir(testdir)
			assert True == False
		except OSError as e:	
			print "dicks"		
			assert True==True
			pass
	

	def cdTest(self):
		
		testdir = "os_test_dir2"
		
		o.mkdir(testdir)
		assert o.xists(testdir)
		o.cd(testdir)
		o.cd("..")

		o.rmdir(testdir)

		assert o.xists(testdir) == False

def suite():
	osSuite=unittest.TestSuite()
	osSuite.addTest(osTestCase("makeTwiceTest"))
	osSuite.addTest(osTestCase("cdTest"))
	return osSuite

testSuite=suite()
result=unittest.TestResult()
testSuite.run(result)
assert result.wasSuccessful
