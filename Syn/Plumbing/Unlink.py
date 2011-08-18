# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber
import Syn.Exceptions
import Syn.Unlink

PLUMBING_NAME = "unlink-package"

def run(args):
	"""
	Unlink a package to the system
	"""
	try:
		Syn.Unlink.unlink(args[2])
	except Syn.Exceptions.SynException as e:
		Syn.Log.l(Syn.Log.CRITICAL,"Exception! %s" % e)
		raise e
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))


Syn.Plumber.registerRoute(PLUMBING_NAME, run)

