"""
Plumber backing code

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Yooooooooooooooooooooook
"""

import Syn.Exceptions

routes = {}

def registerRoute(sysid, run):
	"""
	Register a route for the plumbing to take when invoked.
	@arg sysid: the string to call it by
	@arg run:   the function entry point.
	"""
	routes[sysid] = run

def runRoute(sysid, args):
	"""
	Run route `sysid`, with payload `args`.
	This is called from the syn-plumbing script.
	@arg sysid: ID of the script to invoke
	@arg args:  arguments to pass to the plumbing.
	"""
	try:
		routes[sysid](args)
	except KeyError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("Bad plumbing: %s" % str(e))
