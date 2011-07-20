# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber

PLUMBING_NAME = None

def run(args):
	print "Usage:"
	print ""
	print " Function callback table:"
	for x in Syn.plumber.routes:
		if x != None:
			print "   | %s" % x
	print ""

Syn.plumber.registerRoute(PLUMBING_NAME, run)

