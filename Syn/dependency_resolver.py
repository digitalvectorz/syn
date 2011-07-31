#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.exceptions

def resolveDeps(install, pool):
	key2=pool.viewkeys()
	package_deps=[]
	for x in install:
		package_deps += install[x].getDeps()
	has_deps = key2 & package_deps
	print "has deps",has_deps
	print "key2",key2
	print "package_deps",package_deps
	if(has_deps == set(package_deps)):
		return has_deps
	else:
		raise Syn.exceptions.ArchiveNotFoundException("Can't resolve dep %s" % package_deps);

