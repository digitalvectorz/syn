# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

DATABASE_FILE = ".pkgdb"

NAME_ATTR     = "pkgname"
VERS_ATTR     = "version"
DEPS_ATTR     = "dependencies"
LOCL_ATTR     = "local"
STAT_ATTR     = "status"

STATUS_VALUE  = {
	"HALF-INSTALLED" : "Q",
	"INSTALLED"      : "I",
	"HALF-LINKED"    : "W",
	"LINKED"         : "L",
	"FUCKEDUP"       : "F"
}
