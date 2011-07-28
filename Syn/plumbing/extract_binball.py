# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber

PLUMBING_NAME = "binball-extract"

def run(args):
	"""
	Extract a binary tarball into the CWD
	"""
	try:
		if Syn.sh.xists(args[2]):
			btb = Syn.binary_tarball.binary_tarball(args[2])
			btb.extractall()
		else:
			raise Syn.exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

Syn.plumber.registerRoute(PLUMBING_NAME, run)

