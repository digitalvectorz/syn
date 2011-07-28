"""
Simple shell routines and such
"""

# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.log

import os.path
import shutil
import os

def isRoot():
	"""
	Check if the current user is root, without testing it in any kind
	of nasty way. This might be forgeable, but it's OK.
	"""
	uID = os.geteuid()
	Syn.log.l(Syn.log.PEDANTIC, "euid: " + str(uID))
	ret = uID == 0
	return ret

def mkdir(location):
	"""
	Make a directory, and give some loven.
	"""
	Syn.log.l(Syn.log.PEDANTIC, "creating dir " + location)
	os.makedirs(location)

def cd(work_dir):
	"""
	Change directory to another one.
	"""
	os.chdir(work_dir)
	Syn.log.l(Syn.log.PEDANTIC, "chdir to " + work_dir)

def cp(to, fro):
	"""
	Copy a file from `to' to `fro'.
	"""
	shutil.copy(to, fro)
	Syn.log.l(Syn.log.PEDANTIC, "copy %s %s" % (to, fro))

def mv(to, fro):
	"""
	Move a file from `to' to `fro'
	"""
	shutil.move(to, fro)
	Syn.log.l(Syn.log.PEDANTIC, "move %s %s" % (to, fro))

def isln(loc):
	"""
	Check to see if `loc' is a Simlink or not.
	"""
	Syn.log.l(Syn.log.PEDANTIC, "checking is similink path `%s'" % loc)
	return os.path.islink(loc)

def xists(loc):
	"""
	Check to see if `loc' exists on the filesystem.
	"""
	Syn.log.l(Syn.log.PEDANTIC, "checking path `%s'" % loc)
	return os.path.exists(loc)

def rmdir(dirs):
	"""
	Remove a directory recursively
	"""
	Syn.log.l(Syn.log.PEDANTIC, "rmdir " + dirs)
	shutil.rmtree(dirs)

def rm(dirs):
	"""
	Remove a single file
	"""
	Syn.log.l(Syn.log.PEDANTIC, "rm " + dirs)
	os.remove(dirs)

def ln(source, dest):
	"""
	Simlink a file from `source' to `dest'
	"""
	dirski = os.path.dirname(dest)
	if not xists(dirski):
		Syn.log.l(Syn.log.PEDANTIC, "Can't find it's basedir. Creating it")
		mkdir(dirski)
	Syn.log.l(Syn.log.PEDANTIC, "ln " + source + " to " + dest)
	os.symlink(source, dest)

