#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import unittest
import Syn.goodie_getta as getta

class goodieTestCase(unittest.TestCase):
	def setUp(self):
		self.test=getta.get_goodies(["/usr/bin","/etc"])
		self.test2=getta.get_goodies("/usr/bin")
	def lengthTest(self):
		assert len(self.test2)==1
		assert len(self.test)==2	
	def keyTest(self):
		assert self.test[0].has_key("bin")

		assert self.test[1].has_key("etc")
	
		assert self.test2.has_key("bin")
def suite():
	goodieSuite=unittest.TestSuite()
	goodieSuite.addTest(goodieTestCase("setUp"))
	goodieSuite.addTest(goodieTestCase("lengthTest"))
	goodieSuite.addTest(goodieTestCase("keyTest"))
	return goodieSuite

testSuite=suite()
result=unittest.TestResult()
testSuite.run(result)

assert result.wasSuccessful()

