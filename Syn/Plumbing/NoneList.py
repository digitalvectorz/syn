# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber

PLUMBING_NAME = None

display_blacklist = [
	None,
	"echo",
	"_nukestrap"
]

def run(args):
	"""
	None callback, eacho all routes, except the blacklisted ones.
	"""
	print "Usage:"
	print ""
	print " Function callback table:"
	for x in sorted(Syn.Plumber.routes.iterkeys()):
		if not x in display_blacklist:
			print "   - %s" % x
	print ""

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

