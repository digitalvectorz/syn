# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import gzip

class bfile:
	def __init__(self, fil):
		self.file = fil

	def update(self):
		f = gzip.open(self.file, 'rb')
		self.setContent(f.read())
		f.close()
	def write(self):
		f = gzip.open(self.file, 'wb')
		f.write(self.getContent())
		f.close()

	def setContent(self, content):
		self.content = content
	def getContent(self):
		return self.content
