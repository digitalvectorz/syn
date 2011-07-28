# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber
import Syn.synd

PLUMBING_NAME = "synball-create"

def run(args):
	"""
	Create and package a synball from a syn source directory.
	Note: You should run this where you can see `synd` if you
	run a `ls`.
	"""
	Syn.synd.packageSynd()

Syn.plumber.registerRoute(PLUMBING_NAME, run)

