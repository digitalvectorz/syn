#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.bfile

test_content = """Hello, World!

This is a test of this and that
also this, and that as well. this that
that and the other, with a bit of this and that.
"""

file_id = "bfile-test.testdb"

tfile = Syn.bfile.bfile(file_id)
tfile.setContent(test_content)
tfile.write()

compare_content = tfile.getContent() # basic read test

print "Asserting basic write cache read"
assert compare_content == test_content

tfile2 = Syn.bfile.bfile(file_id)
compare_content_2 = tfile2.getContent() # complex read test

print "Asserting file re-read"

assert test_content == compare_content_2
