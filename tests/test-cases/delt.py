#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>


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

