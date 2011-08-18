# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber

PLUMBING_NAME = "tarball-tld"

def run(args):
	Syn.Log.VERBOSITY = -1
	"""
	Get the tarball's TLD
	"""
	try:
		tb = Syn.Tarball.Tarball(args[2])
		root = tb.getRootFolder()
		print root
	except IndexError as e:
		raise Syn.Exceptions.FileNotPresentException("You can't handle the truth")

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

