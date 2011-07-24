#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.package
import Syn.dependency_resolver

v = "1"

A = Syn.package.package(
	Syn.package.package_attrs("A", v, v, ["B", "C"]))
B = Syn.package.package(
	Syn.package.package_attrs("B", v, v, ["C"]))
C = Syn.package.package(
	Syn.package.package_attrs("C", v, v, ["A", "B"]))
D = Syn.package.package(
	Syn.package.package_attrs("D", v, v, ["A"]))
E = Syn.package.package(
	Syn.package.package_attrs("D", v, v, ["A", "V"]))

INSTALLED_LIST  = { "A" : A, "B" : B, "C" : C }
TO_INSTALL      = { "D" : D    }
TO_INSTALL_FAIL = { "E" : E    }

print "Checking a good resolve:"
DEPS = Syn.dependency_resolver.resolveDeps(TO_INSTALL, INSTALLED_LIST)
print DEPS

try:
	print "Checking a bad resolve:"
	DEPS = Syn.dependency_resolver.resolveDeps(TO_INSTALL_FAIL, INSTALLED_LIST)
	print "Oh shit."
	print DEPS
	assert True == False
except Syn.exceptions.ArchiveNotFoundException as e:
	print "Exception. Good"

