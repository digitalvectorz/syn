# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.exceptions

PLUMBING_NAME = "syns"

def run(args):
	try:
		if Syn.sh.xists(args[2]):
			stb = Syn.source_tarball.source_tarball(args[2])
			otb = stb.upstream_tarball_id()

			frob = stb.get_metablob()

			barfola = {
				"synsource"  : args[2],
				"sourcecode" : otb,
				"package"    : frob['package'],
				"version"    : frob['version']
			}

			jsf = Syn.json_file.json_file("%s-%s.syn.manifest" % (frob['package'], frob['version']))
			jsf.setContent(barfola)
			jsf.write()
		else:
			raise Syn.exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))


Syn.plumber.registerRoute(PLUMBING_NAME, run)

