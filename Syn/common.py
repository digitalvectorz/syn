"""
Common syn routines.
"""
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.universal as U
import Syn.log
import os.path
import time
import os

import commands

def getTempLocation():
	"""
	`getTempLocation` gets a location to play with in the filesystem,
	set up to cause as little harm as one can. This is used to do stuff
	like clean-isolate builds and such. Be sure to clean up after yourself!
	@return: A String containing a path where you can play in.
	"""
	timestamp = time.time()
	unpack_dir = U.TMP_WORKDIR + str(timestamp)
	return unpack_dir

def getTempFileLoc():
	"""
	`getTempFileLoc` allows you to get a temp location to store a file,
	without having to sweat about klobbering this or that. Similar to
	`getTempLocation`, but for files.
	@return: A String containing a path where you can write a file to.
	"""
	timestamp = time.time()
	unpack_dir = U.TMP_WORKDIR + str(timestamp) + "-file"
	return unpack_dir

def getcwd():
	"""
	Get the goddamned current working directory.
	@returns: The directory you're in. Stupid.
	"""
	return os.path.abspath(os.getcwd())

def putenv(key, value):
	"""
	Puts a key/value pair into the env, comes in handy for kicking
	off build-scripts and all that.

	This is similar to the bash call:

	`export key=$value`

	@arg key: What to store the value as
	@arg value: What to store
	"""
	Syn.log.l(Syn.log.VERBOSE, "W: %s = %s" % (key, value))
	os.environ[key] = value

def getenv(key):
	"""
	`getenv` gets a key from the env, great for snagging stuff scripts
	or a bashrc might have pushed out to us. Emails, you name it.

	This is similar to `echo $key`.

	@arg key: Key of what to find
	@return: Value of key
	"""
	value = os.environ[key]
	Syn.log.l(Syn.log.VERBOSE, "R: %s = %s" % (key, value))
	return value

def run(cmd):
	"""
	Run a command on the host. Use this as little as you can.
	@arg cmd: Command to run. This uses the env.
	@return: a tupple containing (status, output).
	"""
	Syn.log.l(Syn.log.VERBOSE, "Running: %s" % cmd)
	return commands.getstatusoutput(cmd)

def getRelativePath(dirname):
	"""
	Get the relitive path to a directory
	@arg dirname: Directory to process.
	@return: the path (relitive to the CWD) to that directory.
	"""
	cur_dir = Syn.common.getcwd()
	test_dir = os.path.relpath(dirname,cur_dir)
	
	return test_dir

def isdict(f):
	"""
	Is the arg passed a dickt?
	@arg f: Object (dict?)
	@return: True if `f` is a dict, False if `f` is **not** a dict.
	"""
	if type(f) is dict:
		return True
	return False

def sortdict(f):
	"""
	Sort the arg
	@arg f: dict object
	@return: sorted dict map
	"""
	keys = f.keys()
	keys.sort()
	return map(f.get, keys)

def delt(arg1,arg2):
	"""
	Generate a delta between two dicts.
	@arg arg1: First dict
	@arg arg2: Second dict
	@return: A dict that contains the delta.
	"""
	assert isdict(arg1)
	assert isdict(arg2)
	a = arg1
	b = arg2
	return dict([
		(key, b.get(key, a.get(key)))
		for key in set(a.keys()+b.keys())
		if (key in a and (not key in b or b[key] != a[key]))
		or (key in b and (not key in a or a[key] != b[key]))
	])

