#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.exceptions

def resolveDeps(install, pool):
	available_packages=[]
	for i in pool:
		available_packages=pool[i].getName()
	package_deps=[]
	for x in install:
		package_deps += install[x].getDeps()
	has_deps = set(available_packages) & set(package_deps)
	if(has_deps == set(package_deps)):
		return has_deps
	else:
		raise Syn.exceptions.ArchiveNotFoundException("Can't resolve dep %s" % package_deps);

