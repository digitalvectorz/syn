#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.package_registry
import Syn.exceptions

pkgdb = Syn.package_registry.package_registry("./test-syn-root")
try:
	pkgdb.getPackage("bash")
	assert True == False
except Syn.exceptions.PackageNotFoundException as e:
	print e

bpatr = Syn.package_registry.package_attrs("bash", 4.3, ["a", "b"])
pkgdb.setPackage("bash",bpatr)

try:
	f = pkgdb.getPackage("bash")
	print f
except Syn.exceptions.PackageNotFoundException as e:
	assert True == False

