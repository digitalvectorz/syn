# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber
import Syn.exceptions
import Syn.install

PLUMBING_NAME = "install-package"

def run(args):
	"""
	Install a binball to the system
	"""
	try:
		if Syn.sh.xists(args[2]):
			Syn.install.install(args[2])
		else:
			raise Syn.exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))


Syn.plumber.registerRoute(PLUMBING_NAME, run)

