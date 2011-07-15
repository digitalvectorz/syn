# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.universal as U
import Syn.log
import time
import os

import commands

def getTempLocation():
	timestamp = time.time()
	unpack_dir = U.TMP_WORKDIR + str(timestamp) + "/"
	return unpack_dir

def putenv(key, value):
	Syn.log.l(Syn.log.VERBOSE, "%s = %s" % (key, value))
	os.putenv(key, value)

def run(cmd):
	return commands.getstatusoutput(cmd)

