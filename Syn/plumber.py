"""
Plumber backing code

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Yooooooooooooooooooooook
"""

import Syn.exceptions

routes = {}

def registerRoute(sysid, run):
	routes[sysid] = run

def runRoute(sysid, args):
	try:
		routes[sysid](args)
	except KeyError as e:
		raise Syn.exceptions.SynShittyPlumbingException("Bad plumbing: %s" % str(e))
