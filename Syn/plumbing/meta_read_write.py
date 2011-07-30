# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumber
import json

def setAttr(meta, string):
	try:
		dot = string.index(".")
		eq = string.index("=")

		if dot > eq:
			raise ValueError("Dummy!")

		fart        = string[:dot]
		masterklass = string[dot+1:]

		ms = setAttr(meta[fart], masterklass)
		return meta
	except ValueError as e:
		try:
			eq = string.index("=")
			val   = string[eq+1:]

			try:
				val = json.loads(val)
				#print "Using the decoded JSON string, and not the string literal"
			except Exception as e:
				pass

			key   = string[:eq]
			meta[key] = val
			return meta
		except ValueError as e:
			print "Invalid attr string! Shit!"
			return None

def getAttr(meta, string):
	try:
		dot      = string.index(".")
		if dot != None:
			nextID   = string[:dot]
			nextPrcs = string[dot+1:]
			subtree = meta[nextID]
			return getAttr(subtree, nextPrcs)
		else:
			raise ValueError("Dummy")
	except ValueError as e:
		return meta[string]



def meta_read(args):
	if len(args) < 4:
		raise Syn.exceptions.SynShittyPlumbingException("Too few arguments")
	f = open(args[2], 'r') # XXX: Default this to synd/metapkg
	meta = json.loads(f.read())
	f.close()
	frob = getAttr(meta, args[3])
	print frob


Syn.plumber.registerRoute("metafile-read", meta_read)

