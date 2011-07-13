#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import Syn.tarball
import os.path

test_tarball = "md5test.tar.gz"
test_root    = "md5test"

t = Syn.tarball.tarball(test_tarball)
root = t.getRootFolder()

def isdict(f):
	if type(f) is dict:
		return True
	return False

def delt(arg1,arg2):
	assert isdict(arg1)
	assert isdict(arg2)
	a = arg1
	b = arg2
	return dict([
		(key, b.get(key, a.get(key)))
		for key in set(a.keys()+b.keys())
		if (key in a and (not key in b or b[key] != a[key]))
		or (key in b and (not key in a or a[key] != b[key]))
	])


print "testing md5"
print t.md5()
#file_id = "md5sums-tarball.txt"

test_dict={'md5test/bar':'5bf487da0233682aa1b52bccbc530ab8',  
	   'md5test/baz':'86cdc6230a4b73b4aa606f27d178979e',
	   'md5test/foo':'26bb73556ceb32a5df30b733c5355ee5'}  


assert delt(t.md5(), test_dict) == {}	

print "md5 works"	


