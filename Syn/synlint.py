"""
Policy error checking

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Obey me.
"""

import Syn.policy.metafile

def evaluateMetadict(crap):
	"""
	Preform baseline synlint metafile checks on a metadict.
	@arg crap: Metafile to run through testing.
	@return: a tupple of counts of errors ( errors, warnings, pendents ).
	"""
	errors   = 0
	warnings = 0
	pendent  = 0

	neededTags = Syn.policy.metafile.META_REQUIRED
	for needed_tag in neededTags:
		try:
			result = crap[needed_tag]
		except KeyError as e:
			errors = errors + 1
			Syn.log.l(Syn.log.CRITICAL,"Missing critical tag: %s!!!" % needed_tag)

	warningTags = Syn.policy.metafile.META_NEEDED
	for warning_tag in warningTags:
		try:
			result = crap[warning_tag]
		except KeyError as e:
			warnings = warnings + 1
			Syn.log.l(Syn.log.HIGH,"Missing needed tag: %s!!!" % warning_tag)

	goodToHaveTags = Syn.policy.metafile.META_GOODTOHAVE
	for tag in goodToHaveTags:
		try:
			result = crap[tag]
		except KeyError as e:
			pendent = pendent + 1
			Syn.log.l(Syn.log.NOTICE, "Missing pendent tag: %s." % tag)

	Syn.log.l(Syn.log.CRITICAL,"")
	Syn.log.l(Syn.log.CRITICAL,"Errors:   %s" % errors)
	Syn.log.l(Syn.log.CRITICAL,"Warnings: %s" % warnings)
	Syn.log.l(Syn.log.CRITICAL,"Pendants: %s" % pendent)
	Syn.log.l(Syn.log.CRITICAL,"")

	return ( errors, warnings, pendent )
