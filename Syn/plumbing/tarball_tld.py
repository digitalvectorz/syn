# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber

PLUMBING_NAME = "tarball-tld"

def run(args):
	Syn.log.VERBOSITY = -1
	"""
	Get the tarball's TLD
	"""
	try:
		tb = Syn.tarball.tarball(args[2])
		root = tb.getRootFolder()
		print root
	except IndexError as e:
		raise Syn.exceptions.FileNotPresentException("You can't handle the truth")

Syn.plumber.registerRoute(PLUMBING_NAME, run)

