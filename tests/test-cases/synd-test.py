#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.sh
import Syn.synd
import Syn.common
import Syn.exceptions
import Syn.source_tarball
import Syn.policy.source_package as S

try:
	Syn.synd.loadEnv()
except Syn.exceptions.SynFormatException as e:
	print "Fuck'n magnets."
	assert True == False

[ status, output ] = Syn.common.run("./test-cases/synd-subtst.sh")

for x in S.BUILD_ENV_KEYS:
	try:
		i = output.index(x)
	except ValueError as e:
		print "Fuck this"
		assert True == False

A = Syn.synd.runStage("configure")
B = Syn.synd.runStage("build")
C = Syn.synd.runStage("stage")

print "Ensuring output tests match"
print A, B, C

assert A == "configure"
assert B == "make -j3"
assert C == "make install"

Syn.source_tarball.source_tarball("test-1.0.syn.tar.gz").extractall()

Syn.sh.cd("test-1.0")
Syn.synd.packageSynd()
