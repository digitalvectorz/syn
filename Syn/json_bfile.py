"""
JSON version of a bfile.
"""
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import json
import gzip
import Syn.bfile
import Syn.log as l

class json_bfile(Syn.bfile.bfile):
	"""
	`json_bfile` stores a JSON dict in a gzip compressed file, for
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
