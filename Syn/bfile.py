"""
Simple binary file module

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 This handles reads and writes to gzip compressed files, if the files
 are large, ior if you know there'll be a bunch of them.
"""

import gzip
import Syn.log as l

class bfile:
	"""
	`bfile` is a simple binary (gzip) compressed
	file, which may be used to compress files that
	make sense to compress.
	"""
	def __init__(self, fil):
		"""
		Simple constructor.
		@arg fil: File to load, or create if it does not exist.
		"""
		self.file = fil
		l.l(l.PEDANTIC,"Using file: %s" % fil)
		try:
			self.update()
			l.l(l.PEDANTIC,"existing file loaded: %s" % fil)
		except IOError as e:
			# OK, we need to create it.
			self.blankFile()

	def blankFile(self):
		"""
		`blankFile` simply blanks out the bfile loaded.
		"""
		l.l(l.PEDANTIC,"creating blank file: %s" % self.file)
		self.setContent("")
		self.write()

	def update(self):
		"""
		`update` syncs the file in the filesystem into this object,
		if the file has been written while the file has been cached
		in memory.
		"""
		l.l(l.PEDANTIC,"Updating file: %s" % self.file)
		f = gzip.open(self.file, 'rb')
		self.setContent(f.read())
		f.close()

	def write(self):
		"""
		`write` writes the cached file to the filesystem, overwriting
		whatever was on that file moments ago.
		"""
		l.l(l.PEDANTIC,"Writing file: %s" % self.file)
		f = gzip.open(self.file, 'wb')
		f.write(self.getContent())
		f.close()

	def setContent(self, content):
		"""
		`setContent` sets the content of the cache, klobbering
		what was there before.
		@arg content: content to cache, and prepare for write.
		"""
		self.content = content
		l.l(l.PEDANTIC,"Setting internal cache: %s" % self.file)

	def getContent(self):
		"""
		`getContent` gets the loaded content for digestion.
		@return: the goodies from the file 
		"""
		return self.content
