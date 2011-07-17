# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.universal as U
import Syn.log
import os.path
import time
import os

import commands

def getTempLocation():
	timestamp = time.time()
	unpack_dir = U.TMP_WORKDIR + str(timestamp) + "/"
	return unpack_dir

def getcwd():
	return os.path.abspath(os.getcwd())

def putenv(key, value):
	Syn.log.l(Syn.log.VERBOSE, "%s = %s" % (key, value))
	os.putenv(key, value)

def run(cmd):
	return commands.getstatusoutput(cmd)

def getRelativePath(dirname):
	cur_dir = Syn.common.getcwd()
	test_dir = os.path.relpath(dirname,cur_dir)
	
	return test_dir
