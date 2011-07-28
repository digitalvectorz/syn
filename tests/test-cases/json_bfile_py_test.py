#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>



import Syn.json_bfile as b
import unittest
import delt

class jsonbfileTestCase(unittest.TestCase):
	def setUp(self):
		file_id = "json_bfile-test.testdb"
		self.jb = b.json_bfile(file_id)
		
	def readTest(self):
		
		test_content = {
			"hillbilly"  : "redneck",
			"hillbilly1" : "redneck",
			"hillbilly2" : "redneck",
			"hillbilly3" : "redneck",
			"hillbilly4" : "redneck"
		}
		self.jb.setContent(test_content)
		self.jb.write()

		compare_content = self.jb.getContent() 

		assert delt.delt(compare_content, test_content) == {}	
	def compareTest(self):
		test_content = {
			"hillbilly"  : "redneck",
			"hillbilly1" : "redneck",
			"hillbilly2" : "redneck",
			"hillbilly3" : "redneck",
			"hillbilly4" : "redneck"
			}
		
		file_id = "json_bfile-test.testdb"

		jb2 = b.json_bfile(file_id)
		cc2 = jb2.getContent()

		assert delt.delt(cc2, test_content) == {}
def suite():
	jsonbfileSuite=unittest.TestSuite()
	jsonbfileSuite.addTest(jsonbfileTestCase("setUp"))
	jsonbfileSuite.addTest(jsonbfileTestCase("readTest"))
	jsonbfileSuite.addTest(jsonbfileTestCase("compareTest"))
	return jsonbfileSuite

testSuite=suite()
result=unittest.TestResult()
testSuite.run(result)

assert result.wasSuccessful()

