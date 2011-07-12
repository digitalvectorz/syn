#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.json_bfile

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

test_content = {
	"hillbilly"  : "redneck",
	"hillbilly1" : "redneck",
	"hillbilly2" : "redneck",
	"hillbilly3" : "redneck",
	"hillbilly4" : "redneck"
}

file_id = "json_bfile-test.testdb"

jb = Syn.json_bfile.json_bfile(file_id)
jb.setContent(test_content)
jb.write()

compare_content = jb.getContent() # basic read test

print "Asserting basic write cache read"

assert delt(compare_content, test_content) == {}

jb2 = Syn.json_bfile.json_bfile(file_id)
cc2 = jb2.getContent()

assert delt(cc2, test_content) == {}
