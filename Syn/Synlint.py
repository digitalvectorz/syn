"""
Policy error checking

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Obey me.
"""

import Syn.Policy.Metafile

def evaluateMetadict(crap):
	"""
	Preform baseline synlint metafile checks on a metadict.
	@arg crap: Metafile to run through testing.
	@return: a tupple of counts of errors ( errors, warnings, pendents ).
	"""
	errors   = 0
	warnings = 0
	pendent  = 0

	neededTags = Syn.Policy.Metafile.META_REQUIRED
	for needed_tag in neededTags:
		try:
			result = crap[needed_tag]
		except KeyError as e:
			errors = errors + 1
			Syn.Log.l(Syn.Log.CRITICAL,"Missing critical tag: %s!!!" % needed_tag)

	warningTags = Syn.Policy.Metafile.META_NEEDED
	for warning_tag in warningTags:
		try:
			result = crap[warning_tag]
		except KeyError as e:
			warnings = warnings + 1
			Syn.Log.l(Syn.Log.HIGH,"Missing needed tag: %s!!!" % warning_tag)

	goodToHaveTags = Syn.Policy.Metafile.META_GOODTOHAVE
	for tag in goodToHaveTags:
		try:
			result = crap[tag]
		except KeyError as e:
			pendent = pendent + 1
			Syn.Log.l(Syn.Log.NOTICE, "Missing pendent tag: %s." % tag)

	Syn.Log.l(Syn.Log.CRITICAL,"")
	Syn.Log.l(Syn.Log.CRITICAL,"Errors:   %s" % errors)
	Syn.Log.l(Syn.Log.CRITICAL,"Warnings: %s" % warnings)
	Syn.Log.l(Syn.Log.CRITICAL,"Pendants: %s" % pendent)
	Syn.Log.l(Syn.Log.CRITICAL,"")

	return ( errors, warnings, pendent )
