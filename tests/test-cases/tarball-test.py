#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.tarball
import os.path

test_tarball = "test-0.1.tar.gz"
test_root    = "test-0.1"

t = Syn.tarball.tarball(test_tarball)
root = t.getRootFolder()

print "asserting root is the same as the read root"
assert test_root == root

print "make sure dir is not present"

assert os.path.exists(test_root) == False
print "OK, extracting"

t.extractall()

print "extracted, testing existance"

assert os.path.exists(test_root) == True
