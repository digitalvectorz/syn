# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber

import Syn.policy.build as B

PLUMBING_NAME = "get-build-blacklist"

def run(args):
	"""
	Get build blacklists.
	"""
	for x in B.FOLDER_BLACKLIST:
		print x

Syn.plumber.registerRoute(PLUMBING_NAME, run)

