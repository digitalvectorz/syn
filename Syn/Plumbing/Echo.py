# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber

PLUMBING_NAME = "echo"

def run(args):
	"""
	Echo!
	Echo!
	"""
	print args

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

