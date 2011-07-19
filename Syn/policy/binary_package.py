# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

#syn/
#  filesums <-- gzip compressed
#  metafile <-- gzip compressed JSON
#  hooks:
#    preinst
#    postinst
#    prerm
#    postrm
#  root:
#    usr...
#    etc...

import Syn.policy.source_package as S

TOP_LEVEL_DIR = "syn"
FILESUMS      = "filesums"
METAFILE      = "metafile"
HOOK_DIR      = "hooks"
FS_ROOT       = S.STAGE_FOLD
META_ROOT     = S.STAGE_META

XTN             = ".syn"

BINARY_DIR_REQ_FILES = [
	META_ROOT + METAFILE
]

