# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber
import Syn.synd

PLUMBING_NAME = "synball-create"

def run(args):
	Syn.synd.packageSynd()

Syn.plumber.registerRoute(PLUMBING_NAME, run)

