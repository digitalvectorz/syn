#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.sh as o

testdir = "os-test-dir"

print "Making: %s" % testdir
o.mkdir(testdir)
try:
	o.mkdir(testdir)
	print "Trying to make it twice"
	assert True == False
except OSError as e:
	pass

assert o.xists(testdir)

o.cd(testdir)
o.cd("..")

o.rmdir(testdir)

assert o.xists(testdir) == False
