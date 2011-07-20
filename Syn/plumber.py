# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.exceptions

routes = {}

def registerRoute(sysid, run):
	routes[sysid] = run

def runRoute(sysid, args):
	try:
		routes[sysid](args)
	except KeyError as e:
		raise Syn.exceptions.SynShittyPlumbingException("Bad plumbing: %s" % str(e))
