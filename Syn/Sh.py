"""
Simple shell stuffs

 @license: GPL-3+
 @author:  Paul Tagliamonte <paultag@gmail.com>
 @date:    August 6th, 2011, 01:50 -0000

 It ain't no bash.
"""
import Syn.Log

import os.path
import shutil
import os

def isRoot():
	"""
	Check if the current user is root, without testing it in any kind
	of nasty way. This might be forgeable, but it's OK.
	"""
	uID = os.geteuid()
	Syn.Log.l(Syn.Log.PEDANTIC, "euid: " + str(uID))
	ret = uID == 0
	return ret

def mkdir(location):
	"""
	Make a directory, and give some loven.
	"""
	Syn.Log.l(Syn.Log.PEDANTIC, "creating dir " + location)
	os.makedirs(location)

def ensuredir(location):
	"""
	Make a directory, and give some loven.
	"""
	if not xists(location):
		Syn.Log.l(Syn.Log.PEDANTIC, "creating dir " + location)
		os.makedirs(location)

def cd(work_dir):
	"""
	Change directory to another one.
	"""
	os.chdir(work_dir)
	Syn.Log.l(Syn.Log.PEDANTIC, "chdir to " + work_dir)

def cp(to, fro):
	"""
	Copy a file from `to' to `fro'.
	"""
	shutil.copy(to, fro)
	Syn.Log.l(Syn.Log.PEDANTIC, "copy %s %s" % (to, fro))

def mv(to, fro):
	"""
	Move a file from `to' to `fro'
	"""
	shutil.move(to, fro)
	Syn.Log.l(Syn.Log.PEDANTIC, "move %s %s" % (to, fro))

def isln(loc):
	"""
	Check to see if `loc' is a Simlink or not.
	"""
	Syn.Log.l(Syn.Log.PEDANTIC, "checking is similink path `%s'" % loc)
	return os.path.islink(loc)

def xists(loc):
	"""
	Check to see if `loc' exists on the filesystem.
	"""
	Syn.Log.l(Syn.Log.PEDANTIC, "checking path `%s'" % loc)
	return os.path.exists(loc)

def rmdir(dirs):
	"""
	Remove a directory recursively
	"""
	Syn.Log.l(Syn.Log.PEDANTIC, "rmdir " + dirs)
	shutil.rmtree(dirs)

def rm(dirs):
	"""
	Remove a single file
	"""
	Syn.Log.l(Syn.Log.PEDANTIC, "rm " + dirs)
	os.remove(dirs)

def ln(source, dest):
	"""
	Simlink a file from `source' to `dest'
	"""
	dirski = os.path.dirname(dest)
	if not xists(dirski):
		Syn.Log.l(Syn.Log.PEDANTIC, "Can't find it's basedir. Creating it")
		mkdir(dirski)
	Syn.Log.l(Syn.Log.PEDANTIC, "ln " + source + " to " + dest)
	os.symlink(source, dest)

