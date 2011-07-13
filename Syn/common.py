# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import time
import Syn.policy.universal as U

def getTempLocation():
	timestamp = time.time()
	unpack_dir = U.TMP_WORKDIR + str(timestamp) + "/"
	return unpack_dir
