# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.Plumber
import Syn.Synlint

import Syn.JsonFile
import Syn.SourceTarball

def runSynlintSynball(args):
	"""
	Check a package for lint issues.
	"""
	try:
		if Syn.Sh.xists(args[2]):
			stb = Syn.SourceTarball.SourceTarball(args[2])
			Syn.Log.l(Syn.Log.VERBOSE,"TLD Resolved as: %s" % stb.getRootFolder())
			dickt = stb.getMetablob()
			( errors, warnings, pendent ) = Syn.Synlint.evaluateMetadict(dickt)
		else:
			raise Syn.Exceptions.SynShittyPlumbingException("Synball does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))

def runSynlintJson(args):
	"""
	Check a metafile for lint issues, be happy.
	"""
	try:
		if Syn.Sh.xists(args[2]):
			jf = Syn.JsonFile.JsonFile(args[2])
			dickt = jf.getContent()
			( errors, warnings, pendent ) = Syn.Synlint.evaluateMetadict(dickt)
		else:
			raise Syn.Exceptions.SynShittyPlumbingException("JSON file does not exist!: %s" % args[2])
	except IndexError as e:
		raise Syn.Exceptions.SynShittyPlumbingException("You forgot an argument!: %s" % str(e))


Syn.Plumber.registerRoute("synlint-synball" , runSynlintSynball)
Syn.Plumber.registerRoute("synlint-metafile", runSynlintJson)

