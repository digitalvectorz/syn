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
	"""
	Basic tarball object. We use this to provide useful features
	to the source / binary tarball objects.
	"""
	def __init__(self, tarball):
		"""
		Basic constructor.
		@arg tarball: tarball to load up.
		"""
		self.tarball = tarball
		self.tarball_target = tarfile.open(tarball, 'r')
		Syn.log.l(Syn.log.VERBOSE, "attempting to load %s" % tarball )
		self.verify()

	def add(self, path, altname=None):
		"""
		A wrapped composed call to `tarfile.add`,
		which is super simplified. Both `altname` and
		`path` are treated the same as `.add`.
		@arg path: path to the file to add.
		@arg altname: altname for the file
		"""
		self.tarball_target.add(
			path,
			arcname   = altname,
			recursive = True,
			exclude   = None,
			filter    = None)

	def getRootFolder(self):
		"""
		Parse every single file in the tarball to get the root
		directory of the archive. This can be super useful to us for loads
		of reasons and things.
		@warning: this may or many not have the slash. deslash it.
		@return: The top-level prefix. "/" or "fluxbox-1.3.1/" are two examples.
		"""
		members = self.tarball_target.getmembers()
		directories = []
		for member in members:
			directories.append(member.name)
		root_folder = os.path.commonprefix(directories)
		return root_folder

	def extractall(self, path = "."):
		"""
		Extract an archive to the CWD.
		@arg path: extract the archive to this path, and not the CWD.
		"""
		self.tarball_target.extractall(path)

	def close(self):
		"""
		Close a tarball file out.
		"""
		self.tarball_target.close()

	def verify(self):
		"""
		Overriden for source / binary tarballs.
		"""
		pass

	def readMember(self, member):
		"""
		Read a single file's goodies, useful for snagging stuff like
		un-gziped metafiles and such.
		@return: that file's content.
		"""
		filename = self.tarball_target.extractfile(member)
		return filename
