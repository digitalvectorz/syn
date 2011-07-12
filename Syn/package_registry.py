# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.log as l
import Syn.json_bfile as flatfile

import Syn.policy.package_registry as R
import Syn.policy.universal        as U

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

class package_registry.py:
	def __init__(self):
		dflt_root = U.SLASH_TOP_LEVEL_DIR
		self.ff = flatfile.json_bfile()
