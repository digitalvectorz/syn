#
# Copyright (c) Paul Tagliamonte
# GNU GPL-3+, 2011
#

CRITICAL = 0 # So critical, we disturb the user during sex
HIGH     = 1 # Ignore anyone in the room to get this message
MESSAGE  = 2 # Watch the spew carefully for these
NOTICE   = 3 # Cool nugget of information we'd like to let the user know about
LOG      = 4 # Bare minimum needed to notify someone of the state of the app
VERBOSE  = 5 # Bare minimum needed to debug the app during normal use
PEDANTIC = 6 # Know about every call made to any function at all points.

HR_LOGLEVELS = {
	CRITICAL : "Critical ",
	HIGH     : "High     ",
	MESSAGE  : "Message  ",
	NOTICE   : "Notice   ",
	LOG      : "Log      ",
	VERBOSE  : "Verbose  ",
	PEDANTIC : "Pedantic "
}

DEFAULT   = PEDANTIC
VERBOSITY = DEFAULT

def l(level, msg):
	if level <= VERBOSITY:
		print "[l] (" + HR_LOGLEVELS[level] + "): " + msg;
def p(msg):
	level = NOTICE
	if level <= VERBOSITY:
		print msg

