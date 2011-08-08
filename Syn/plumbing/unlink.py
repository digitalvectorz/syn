# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber
import Syn.exceptions
import Syn.unlink

PLUMBING_NAME = "unlink-package"

def run(args):
	"""
	Unlink a package to the system
	"""
	try:
		Syn.unlink.unlink(args[2])
	except Syn.exceptions.SynException as e:
		Syn.log.l(Syn.log.CRITICAL,"Exception! %s" % e)
		raise e
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))


Syn.plumber.registerRoute(PLUMBING_NAME, run)

