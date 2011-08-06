"""
Simple JSON File shaznit.

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Create, Read, Update, Blank a JSON plain-text file. 
"""

import json
import Syn.log as l

class json_file():
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
		self.setContent({})
		self.write()

	def update(self):
		l.l(l.PEDANTIC,"Updating JSON file: %s" % self.file)
		f = open(self.file, 'rb')
		self.setContent(json.loads(f.read()))
		f.close()

	def write(self):
		l.l(l.PEDANTIC,"Writing JSON file: %s" % self.file)
		f = open(self.file, 'wb')
		f.write(json.dumps(self.getContent()))
		f.close()

	def setContent(self, content):
		self.content = content
		l.l(l.PEDANTIC,"Setting internal cache: %s" % self.file)
	def getContent(self):
		return self.content
