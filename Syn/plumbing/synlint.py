# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber
import Syn.synlint

import Syn.json_file
import Syn.source_tarball

def run_synlint_synball(args):
	try:
		if Syn.sh.xists(args[2]):
			stb = Syn.source_tarball.source_tarball(args[2])
			dickt = stb.get_metablob()
			( errors, warnings, pendent ) = Syn.synlint.evaluateMetadict(dickt)
		else:
			raise Syn.exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

def run_synlint_json(args):
	try:
		if Syn.sh.xists(args[2]):
			jf = Syn.json_file.json_file(args[2])
			dickt = jf.getContent()
			( errors, warnings, pendent ) = Syn.synlint.evaluateMetadict(dickt)
		else:
			raise Syn.exceptions.SynShittyPlumbingException("JSON file does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))


Syn.plumber.registerRoute("synlint-synball" , run_synlint_synball)
Syn.plumber.registerRoute("synlint-metafile", run_synlint_json)

