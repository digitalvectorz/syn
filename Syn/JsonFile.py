"""
Simple JSON File shaznit.

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Create, Read, Update, Blank a JSON plain-text file. 
"""

import json
import Syn.Log as l

class JsonFile():
	"""
	JSON Flat file abstraction class
	"""
	def __init__(self, fil):
		"""
		Basic run of the mill constructor
		@param fil: File to use
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
		`blankFile` blanks a file.
		"""
		l.l(l.PEDANTIC,"creating blank file: %s" % self.file)
		self.setContent({})
		self.write()

	def update(self):
		"""
		Update re-reads the file from the filesystem
		and updates it's internal cache.
		"""
		l.l(l.PEDANTIC,"Updating JSON file: %s" % self.file)
		f = open(self.file, 'rb')
		self.setContent(json.loads(f.read()))
		f.close()

	def write(self):
		"""
		Write writes out the cache to the filesystem,
		klobbering whatever's there without shame or
		second thought.
		"""
		l.l(l.PEDANTIC,"Writing JSON file: %s" % self.file)
		f = open(self.file, 'wb')
		f.write(json.dumps(self.getContent()))
		f.close()

	def setContent(self, content):
		"""
		Set the internal cache. Might want to use this
		with the `getContent` method.
		@param content: the content to set the cache to.
		"""
		self.content = content
		l.l(l.PEDANTIC,"Setting internal cache: %s" % self.file)

	def getContent(self):
		"""
		Get the internal cache.
		@warning: This may be out of date with the filesystem! Lock DBs!
		@return: A dict of data.
		"""
		return self.content
