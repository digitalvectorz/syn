# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber
import Syn.Synd
import Syn.Sh

PLUMBING_NAME = "synball-compile"

def run(args):
	"""
	**Needed argument**: path to a synball

	Compile a Syn sourceball (synball) in the
	current working directory. 
	"""
	try:
		if Syn.Sh.xists(args[2]):
			Syn.Synd.build(args[2])
		else:
			raise Syn.Exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except Syn.Exceptions.BuildFailureException as e:
		print "Build failure!!!! %s" % e
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

Syn.Plumber.registerRoute(PLUMBING_NAME, run)

