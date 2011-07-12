# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.log as l
import Syn.json_bfile as flatfile

import Syn.policy.package_registry as R
import Syn.policy.universal        as U

import Syn.exceptions

#
# root
#  +-> package_name
#         +-> installed_status : foo
#         +-> version          : 0.0
#         +-> deps
#               +-> foo
#               +-> bar
#               +-> baz
#

class package_registry:
	def __init__(self, path=None):
		if path == None:
			path = U.SLASH_TOP_LEVEL_DIR
		path = path + "/" + R.DATABASE_FILE
		self.__loaddb(path)

	def __loaddb(self, path):
		try:
			self.ff = flatfile.json_bfile(path)
		except IOError as e:
			l.l(l.CRITICAL,"Database does not exist.")
			raise Syn.exceptions.SynDirectoryFailure("%s does not exist." % path)
