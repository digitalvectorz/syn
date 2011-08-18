"""
JSON version of a bfile

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Load and write to a JOSN B-File. Should be gzip compressed.
"""

import json
import gzip
import Syn.Bfile
import Syn.Log as l

class JsonBfile(Syn.Bfile.Bfile):
	"""
	`JsonBfile` stores a JSON dict in a gzip compressed file, for
	pickling and eventual recovery.
	"""

	def blankFile(self):
		"""
		@see: bfile.bfile.blankFile
		"""
		l.l(l.PEDANTIC,"creating blank file: %s" % self.file)
		self.setContent({})
		self.write()

	def update(self):
		"""
		@see: bfile.bfile.update
		"""
		l.l(l.PEDANTIC,"Updating JSON file: %s" % self.file)
		f = gzip.open(self.file, 'rb')
		self.setContent(json.loads(f.read()))
		f.close()

	def write(self):
		"""
		@see: bfile.bfile.write
		"""
		l.l(l.PEDANTIC,"Writing JSON file: %s" % self.file)
		f = gzip.open(self.file, 'wb')
		f.write(json.dumps(self.getContent()))
		f.close()
