# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Exceptions
import Syn.Plumber
import Syn.Log

PLUMBING_NAME = "synball-pkgfullid"

def run(args):
	"""
	Get the package's fullid. Verbosity on logging
	has been set to super-quiet (Milford Academy mode)
	so this can be safely used in bash-subcommand syntax.
	"""
	Syn.Log.VERBOSITY = -1
	try:
		if Syn.Sh.xists(args[2]):
			stb = Syn.SourceTarball.SourceTarball(args[2])
			otb = stb.getPackageFullId()
			print otb
		else:
			raise Syn.Exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

