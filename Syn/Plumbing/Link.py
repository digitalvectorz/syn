# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber
import Syn.Exceptions
import Syn.Link

PLUMBING_NAME = "link-package"

def run(args):
	"""
	Install a package to the system
	"""
	try:
		Syn.Link.link(args[2])
	except Syn.Exceptions.SynException as e:
		Syn.Log.l(Syn.Log.CRITICAL,"Exception! %s" % e)
		raise e
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))


Syn.Plumber.registerRoute(PLUMBING_NAME, run)

