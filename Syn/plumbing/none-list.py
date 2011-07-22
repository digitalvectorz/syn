# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber

PLUMBING_NAME = None

display_blacklist = [
	None,
	"echo",
	"_nukestrap"
]

def run(args):
	print "Usage:"
	print ""
	print " Function callback table:"
	for x in sorted(Syn.plumber.routes.iterkeys()):
		if not x in display_blacklist:
			print "   - %s" % x
	print ""

Syn.plumber.registerRoute(PLUMBING_NAME, run)

