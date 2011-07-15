#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.exceptions

def resolveDeps(install, pool):
	staged_packages = install.copy()
	for x in install:
		package_deps = install[x].getDeps()
		for dep in package_deps:
			try:
				staged_packages[dep] = pool[dep]
			except KeyError as e:
				raise Syn.exceptions.ArchiveNotFoundException("Can't resolve dep %s" % dep);
	if install != staged_packages:
		return resolveDeps(staged_packages, pool)
	else:
		return staged_packages
