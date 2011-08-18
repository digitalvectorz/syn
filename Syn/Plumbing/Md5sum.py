# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Md5sum

PLUMBING_NAME = "md5sum-dir"

def run(args):
	"""
	Produce a syn-formatted md5sum of a directory.
	"""
	try:
		if Syn.Sh.xists(args[2]) and not Syn.Sh.xists(args[3]):
			Syn.Md5sum.createMd5HashFile(args[2], args[3])
		else:
			raise Syn.Exceptions.SynShittyPlumbingException("Barfing Dir: (%s), File: (%s)" % ( args[2], args[3] ) )
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

