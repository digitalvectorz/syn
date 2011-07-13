# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import json
import gzip
import Syn.bfile
import Syn.log as l

class json_bfile(Syn.bfile.bfile):
	def blankFile(self):
		l.l(l.PEDANTIC,"creating blank file: %s" % self.file)
		self.setContent({})
		self.write()

	def update(self):
		l.l(l.PEDANTIC,"Updating JSON file: %s" % self.file)
		f = gzip.open(self.file, 'rb')
		self.setContent(json.loads(f.read()))
		f.close()

	def write(self):
		l.l(l.PEDANTIC,"Writing JSON file: %s" % self.file)
		f = gzip.open(self.file, 'wb')
		f.write(json.dumps(self.getContent()))
		f.close()
