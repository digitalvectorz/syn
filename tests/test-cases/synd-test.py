#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.synd
import Syn.common
import Syn.exceptions
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

