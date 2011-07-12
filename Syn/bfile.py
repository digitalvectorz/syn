# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import gzip
import Syn.log as l

class bfile:
	def __init__(self, fil):
		self.file = fil
		l.l(l.PEDANTIC,"Using file: %s" % fil)
		try:
			self.update()
			l.l(l.PEDANTIC,"existing file loaded: %s" % fil)
		except IOError as e:
			# OK, we need to create it.
			self.blankFile()

	def blankFile(self):
		l.l(l.PEDANTIC,"creating blank file: %s" % self.file)
		self.setContent("")
		self.write()

	def update(self):
		l.l(l.PEDANTIC,"Updating file: %s" % self.file)
		f = gzip.open(self.file, 'rb')
		self.setContent(f.read())
		f.close()

	def write(self):
		l.l(l.PEDANTIC,"Writing file: %s" % self.file)
		f = gzip.open(self.file, 'wb')
		f.write(self.getContent())
		f.close()

	def setContent(self, content):
		self.content = content
		l.l(l.PEDANTIC,"Setting internal cache: %s" % self.file)
	def getContent(self):
		return self.content
