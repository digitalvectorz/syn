# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

#package-N.M
#  synd/
#    hooks/
#      preinst
#      postinst
#      prerm
#      postrm
#    build # makefile to build source
#    build.env # env vars in JSON
#    pkgmeta # metafile for package details (see A2)

SOURCE_DIRECTORY = "synd"
BUILDFILE        = "build"
ENVFILE          = "build.env"
METAFILE         = "metapkg"

SOURCE_DIR_REQ_FILES = [
	BUILDFILE,
	ENVFILE,
	METAFILE
]

STRIP_BINARIES  = "S_STRIP_BINARIES"
CONFIGURE       = "S_CONFIGURE"
CONFIGURE_FLAGS = "S_CONFIGURE_FLAGS"
BUILD           = "S_BUILD"
BUILD_FLAGS     = "S_BUILD_FLAGS"
STAGE           = "S_STAGE"
STAGE_FLAGS     = "S_STAGE_FLAGS"
DESTDIR         = "S_DESTDIR"
BINARY_ROOT     = "S_BINARY_ROOT"

XTN             = ".syn.tar.gz"

STAGE_ROOT      = "./" + SOURCE_DIRECTORY + "/stage"
STAGE_FOLD      = "root"
STAGE_META      = "meta"

BUILD_ENV_KEYS = [
	STRIP_BINARIES,
	CONFIGURE,
	CONFIGURE_FLAGS,
	BUILD,
	BUILD_FLAGS,
	STAGE,
	STAGE_FLAGS
]
