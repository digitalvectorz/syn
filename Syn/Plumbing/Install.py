# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber
import Syn.Exceptions
import Syn.Install

PLUMBING_NAME = "install-package"

def run(args):
	"""
	Install a binball to the system
	"""
	try:
		if Syn.Sh.xists(args[2]):
			Syn.Install.install(args[2])
		else:
			raise Syn.Exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))


Syn.Plumber.registerRoute(PLUMBING_NAME, run)

