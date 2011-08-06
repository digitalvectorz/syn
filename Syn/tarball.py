"""
Simple Tarbal stuffs

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 CRUD type tarball stuff
"""


import Syn.log
import tarfile
import hashlib
import os.path

class tarball:
	def __init__(self, tarball):
		self.tarball = tarball
		self.tarball_target = tarfile.open(tarball, 'r')
		Syn.log.l(Syn.log.VERBOSE, "attempting to load %s" % tarball )
		self.verify()

	def add(self, path, altname=None):
		self.tarball_target.add(
			path,
			arcname   = altname,
			recursive = True,
			exclude   = None,
			filter    = None)

	def getRootFolder(self):
		members = self.tarball_target.getmembers()
		directories = []
		for member in members:
			directories.append(member.name)
		root_folder = os.path.commonprefix(directories)
		return root_folder

	def extractall(self, path = "."):
		self.tarball_target.extractall(path)

	def close(self):
		self.tarball_target.close()

	def verify(self):
		pass

	def readMember(self, member):
		filename = self.tarball_target.extractfile(member)
		return filename

	def md5(self):
		fs = "./meta/filesums"
		returnme = {}
		for member in self.tarball_target.getmembers():
			if member.isdir() == False:
				filename = self.readMember(member)
				m = hashlib.md5()
				while True:
					hash = filename.read(1024)
					if not hash:
						break
					m.update(hash)
				returnme[unicode("./" + member.name)] = unicode(m.hexdigest())
		if returnme.has_key(fs):
			del returnme[fs]
		return returnme
