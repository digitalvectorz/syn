# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.log
import tarfile
import hashlib
import os.path

class tarball:
	def __init__(self, tarball):
		self.tarball = tarball
		self.tarball_target = tarfile.open(tarball, 'r')
		Syn.log.l(Syn.log.VERBOSE, "attempting to load %s" % tarball )

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

	def md5(self):
		returnme = {}
		
		for member in self.tarball_target.getmembers():
			if member.isdir() == False:
				filename = self.tarball_target.extractfile(member)
				m = hashlib.md5()
				while True:
					hash = filename.read(1024)
					if not hash:
						break
					m.update(hash)
				returnme[member.name] = m.hexdigest()
		return returnme
