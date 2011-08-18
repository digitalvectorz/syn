# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber
import Syn.Synd

PLUMBING_NAME = "synball-create"

def run(args):
	"""
	Create and package a synball from a syn source directory.
	Note: You should run this where you can see `synd` if you
	run a `ls`.
	"""
	Syn.Synd.packageSynd()

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

