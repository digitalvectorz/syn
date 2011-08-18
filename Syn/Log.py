"""
Logging made fun

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 Handle logging in a sane way
"""

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
	"""
	Log a message to the default logging target.
	This may be a file, stdout or the network.
	@param level: How critical the alert is
	@param msg: message to send to the target
	"""
	if level <= VERBOSITY:
		print "[l] (" + HR_LOGLEVELS[level] + "): " + msg;
def p(msg):
	"""
	Something stupid, I'm sure.
	"""
	level = NOTICE
	if level <= VERBOSITY:
		print msg

