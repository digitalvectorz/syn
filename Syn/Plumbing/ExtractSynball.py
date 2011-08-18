# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber

PLUMBING_NAME = "synball-extract"

def run(args):
	"""
	Extract a synball to the CWD.
	"""
	try:
		if Syn.Sh.xists(args[2]):
			stb = Syn.SourceTarball.SourceTarball(args[2])
			stb.extractall()
		else:
			raise Syn.Exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

