# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber

PLUMBING_NAME = "build_package"

def run(args):
	print args

Syn.plumber.registerRoute(PLUMBING_NAME, run)

