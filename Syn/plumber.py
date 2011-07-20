# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

routes = {}

def registerRoute(sysid, run):
	routes[sysid] = run

def runRoute(sysid, args):
	routes[sysid](args)
