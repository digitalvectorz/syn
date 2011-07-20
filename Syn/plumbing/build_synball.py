# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber
import Syn.synd
import Syn.sh

PLUMBING_NAME = "build_synball"

def run(args):
	if Syn.sh.xists(args[2]):
		Syn.synd.build(args[2])

Syn.plumber.registerRoute(PLUMBING_NAME, run)

