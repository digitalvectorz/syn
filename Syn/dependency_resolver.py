"""
Resolve dependencies in a super sane way

 @license: GPL-3+
 @author:  Ryan Maloney <rpm5779@rit.edu>
 @date:    August 6th, 2011, 01:50 -0000
 
 Use a super awesome algorithm to resolve runtime dependencies
 and have some fun :)
"""

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

