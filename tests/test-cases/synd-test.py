#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.synd
import Syn.common
import Syn.exceptions
import Syn.policy.source_package as S
import unittest

class syndTestCase(unittest.TestCase):
	def loadTest(self):
		try:
			Syn.synd.loadEnv()
			
		except Syn.exceptions.SynFormatException as e:
			assert True == False
	def runTest(self):
		[ status, output ] = Syn.common.run("./test-cases/synd-subtst.sh")

		for x in S.BUILD_ENV_KEYS:
			try:
				i = output.index(x)
			except ValueError as e:
				print "Fuck this"
				assert True == False
	def runStageTest(self):
		A = Syn.synd.runStage("configure")
		B = Syn.synd.runStage("build")
		C = Syn.synd.runStage("stage")

		print "Ensuring output tests match"
		print A, B, C

		assert A == "configure"
		assert B == "make -j3"
		assert C == "make install"
def suite():
	syndTestSuite=unittest.TestSuite()
	syndTestSuite.addTest(syndTestCase("loadTest"))
	syndTestSuite.addTest(syndTestCase("runTest"))
	syndTestSuite.addTest(syndTestCase("runStageTest"))
	return syndTestSuite

testSuite=suite()
result=unittest.TestResult()
testSuite.run(result)


assert result.wasSuccessful()
