# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.metafile

def evaluateMetadict(crap):
	errors   = 0
	warnings = 0

	neededTags = Syn.policy.metafile.META_REQUIRED
	for needed_tag in neededTags:
		try:
			result = crap[needed_tag]
		except KeyError as e:
			errors = errors + 1
			Syn.log.l(Syn.log.CRITICAL,"Missing critical tag: %s!!!" % needed_tag)

	Syn.log.l(Syn.log.CRITICAL,"")
	Syn.log.l(Syn.log.CRITICAL,"")
	Syn.log.l(Syn.log.CRITICAL,"Errors:   %s" % errors)
	Syn.log.l(Syn.log.CRITICAL,"Warnings: %s" % warnings)
	Syn.log.l(Syn.log.CRITICAL,"")
	Syn.log.l(Syn.log.CRITICAL,"")
