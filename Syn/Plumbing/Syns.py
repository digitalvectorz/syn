# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Exceptions
import Syn.Plumber

PLUMBING_NAME = "syns"

def run(args):
	"""
	To be honest I forget what this does. Fuck it.
	"""
	try:
		if Syn.Sh.xists(args[2]):
			stb = Syn.SourceTarball.SourceTarball(args[2])
			otb = stb.getUpstreamTarballId()

			frob = stb.getMetablob()

			barfola = {
				"synsource"  : args[2],
				"sourcecode" : otb,
				"package"    : frob['package'],
				"version"    : frob['version']
			}

			jsf = Syn.JsonFile.JsonFile("%s-%s.syn.manifest" % (frob['package'], frob['version']))
			jsf.setContent(barfola)
			jsf.write()
		else:
			raise Syn.Exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))


Syn.Plumber.registerRoute(PLUMBING_NAME, run)

