# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Policy.Db as D

import Syn.PackageRegistry
import Syn.Plumber
import Syn.Sh

PLUMBING_NAME = "_nukestrap"

# Need to add in reset-able roots

PREFIX = ""

def run(args):
	"""
	@WARNING: DO NOT USE ME.
	DO NOT USE THIS FUNCTION.
	**SERIOUSLY**. BABIES WILL DIE, YOUR SYSTEM WILL CRY,
	AND I'LL FIND YOU, GUY.

	SERIOUSLY
	"""
	ROOT_PATH = PREFIX + D.DB_ROOT
	if not Syn.Sh.xists(ROOT_PATH):
		Syn.Sh.mkdir(ROOT_PATH)
	Syn.PackageRegistry.do_not_call_me_nukestrap_database_files(ROOT_PATH)

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

