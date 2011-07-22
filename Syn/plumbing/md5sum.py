# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.md5sum

PLUMBING_NAME = "md5sum-dir"

def run(args):
	try:
		if Syn.sh.xists(args[2]) and not Syn.sh.xists(args[3]):
			Syn.md5sum.makemd5sumfile(args[2], args[3])
		else:
			raise Syn.exceptions.SynShittyPlumbingException("Barfing Dir: (%s), File: (%s)" % ( args[2], args[3] ) )
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

Syn.plumber.registerRoute(PLUMBING_NAME, run)

