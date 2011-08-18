#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import unittest
import Syn.Package
import Syn.Exceptions
import Syn.DependencyResolver

class dependencyTestCase(unittest.TestCase):
	def setUp(self):
		pass

	def testDependency(self):
		v = "1"

		A = Syn.Package.package(Syn.Package.package_attrs("A", v, v, ["B", "C"]))
		B = Syn.Package.package(Syn.Package.package_attrs("B", v, v, ["C"]))
		C = Syn.Package.package(Syn.Package.package_attrs("C", v, v, ["A", "B"]))
		D = Syn.Package.package(Syn.Package.package_attrs("D", v, v, ["A"]))
		E = Syn.Package.package(Syn.Package.package_attrs("D", v, v, ["A", "V"]))

		INSTALLED_LIST  = { "A" : A, "B" : B, "C" : C }
		TO_INSTALL      = { "D" : D    }
		TO_INSTALL_FAIL = { "E" : E    }
		try:
			print "Checking a bad resolve:"
			DEPS = Syn.DependencyResolver.resolveDeps(TO_INSTALL_FAIL,INSTALLED_LIST)
			print "Oh shit."
			print DEPS
			assert True == False
		except Syn.Exceptions.ArchiveNotFoundException as e:
			print "Exception. Good"
			assert True==True

if __name__ == '__main__':
	unittest.main()

