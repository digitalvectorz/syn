#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import Syn.package_registry
import Syn.exceptions
import unittest
class packageTestCase(unittest.TestCase):
	def rootTest(self):
		pkgdb = Syn.package_registry.package_registry("./test-syn-root")
		try:
			pkgdb.getPackage("bash")
			assert True == False
		except Syn.exceptions.PackageNotFoundException as e:
			assert True==True

	def listTest(self):
		pkgdb = Syn.package_registry.package_registry("./test-syn-root")
		bpatr = Syn.package_registry.package_attrs("bash", 4.3, 1, ["a", "b"])
		pkgdb.setPackage("bash",bpatr)

		try:
			f = pkgdb.getPackage("bash")
			print f
			pkgdb.setPackage("bash", f)
			assert True==True
		except Syn.exceptions.PackageNotFoundException as e:
			assert True == False
def suite():
	packageTestSuite=unittest.TestSuite()
	packageTestSuite.addTest(packageTestCase("rootTest"))
	packageTestSuite.addTest(packageTestCase("listTest"))
	return packageTestSuite


testSuite=suite()
result=unittest.TestResult()
testSuite.run(result)


assert result.wasSuccessful()
