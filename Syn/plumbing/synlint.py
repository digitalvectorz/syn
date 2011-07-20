# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber
import Syn.synlint

PLUMBING_NAME = "synlint"

def run(args):
	Syn.synlint.evaluateMetadict({
		"package" : "foo"
	})

Syn.plumber.registerRoute(PLUMBING_NAME, run)

