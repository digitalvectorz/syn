# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber

PLUMBING_NAME = "binball-extract"

def run(args):
	"""
	Extract a binary tarball into the CWD
	"""
	try:
		if Syn.Sh.xists(args[2]):
			btb = Syn.BinaryTarball.BinaryTarball(args[2])
			btb.extractall()
		else:
			raise Syn.Exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

