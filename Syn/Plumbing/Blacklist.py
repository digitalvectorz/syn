# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber

import Syn.Policy.Build as B

PLUMBING_NAME = "get-build-blacklist"

def run(args):
	"""
	Get build blacklists.
	"""
	for x in B.FOLDER_BLACKLIST:
		print x

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

