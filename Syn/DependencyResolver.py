"""
Resolve dependencies in a super sane way

 @license: GPL-3+
 @author:  Ryan Maloney <rpm5779@rit.edu>
 @date:    August 6th, 2011, 01:50 -0000
 
 Use a super awesome algorithm to resolve runtime dependencies
 and have some fun :)
"""

import Syn.Exceptions

def resolveDeps(install, pool):
	"""
	`resolveDeps` resolves dependencies of the `install`
	param, using the `pool` argument, which contains all
	packages that we know about.
	@param install: Package set to install
	@param pool:    All packages we know about
	@return: a dict of what needs to be installed
	"""
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
		raise Syn.Exceptions.ArchiveNotFoundException("Can't resolve dep %s" % package_deps);

