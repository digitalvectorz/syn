#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.source_tarball


stb = Syn.source_tarball.source_tarball("test-1.0.syn.tar.gz")

try:
	stb2 = Syn.source_tarball.source_tarball("test-1.0-bad.syn.tar.gz")
	assert True == False
except Syn.exceptions.SynFormatException as e:
	print "Failed with glee"
