#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import unittest
import Syn.bfile
import Syn.sh

class BfileTestCase(unittest.TestCase):
	def setUp(self):		
		self.tfile = Syn.bfile.bfile("bfile-test.testdb")

	def tearDown(self):
		Syn.sh.rm("bfile-test.testdb")

	def test_read(self):
		file_id = "bfile-test.testdb"
		test_content = """Hello, World!
		This is a test of this and that
		also this, and that as well. this that
		that and the other, with a bit of this and that.
		"""
		self.tfile.setContent(test_content)
		self.tfile.write()
		compare_content = self.tfile.getContent() 
		assert compare_content == test_content

		tfile2 = Syn.bfile.bfile(file_id)
		compare_content_2 = tfile2.getContent() 
		assert test_content == compare_content_2

if __name__ == '__main__':
	unittest.main()
