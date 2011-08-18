"""
Simple Tarbal stuffs

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 CRUD type Tarball stuff
"""


import Syn.Log
import tarfile
import hashlib
import os.path

class Tarball:
	"""
	Basic Tarball object. We use this to provide useful features
	to the source / binary Tarball objects.
	"""
	def __init__(self, Tarball):
		"""
		Basic constructor.
		@arg Tarball: Tarball to load up.
		"""
		self.Tarball = Tarball
		self.Tarball_Target = tarfile.open(Tarball, 'r')
		Syn.Log.l(Syn.Log.VERBOSE, "attempting to load %s" % Tarball )
		self.verify()

	def add(self, path, altname=None):
		"""
		A wrapped composed call to `tarfile.add`,
		which is super simplified. Both `altname` and
		`path` are treated the same as `.add`.
		@arg path: path to the file to add.
		@arg altname: altname for the file
		"""
		self.Tarball_Target.add(
			path,
			arcname   = altname,
			recursive = True,
			exclude   = None,
			filter    = None)

	def getRootFolder(self):
		"""
		Parse every single file in the Tarball to get the root
		directory of the archive. This can be super useful to us for loads
		of reasons and things.
		@warning: this may or many not have the slash. deslash it.
		@return: The top-level prefix. "/" or "fluxbox-1.3.1/" are two examples.
		"""
		members = self.Tarball_Target.getmembers()
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
		self.Tarball_Target.extractall(path)

	def close(self):
		"""
		Close a Tarball file out.
		"""
		self.Tarball_Target.close()

	def verify(self):
		"""
		Overriden for source / binary Tarballs.
		"""
		pass

	def readMember(self, member):
		"""
		Read a single file's goodies, useful for snagging stuff like
		un-gziped metafiles and such.
		@return: that file's content.
		"""
		filename = self.Tarball_Target.extractfile(member)
		return filename
