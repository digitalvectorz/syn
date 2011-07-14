# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.log

import os.path
import shutil
import os

def isRoot():
	uID = os.geteuid()
	Syn.log.l(Syn.log.PEDANTIC, "euid: " + str(uID))
	ret = uID == 0
	return ret
def mkdir(location):
	Syn.log.l(Syn.log.PEDANTIC, "creating dir " + location)
	os.makedirs(location)
def cd(work_dir):
	os.chdir(work_dir)
	Syn.log.l(Syn.log.PEDANTIC, "chdir to " + work_dir)
def cp(to, fro):
	shutil.copy(to, fro)
	Syn.log.l(Syn.log.PEDANTIC, "copy %s %s" % (to, fro))
def mv(to, fro):
	shutil.move(to, fro)
	Syn.log.l(Syn.log.PEDANTIC, "move %s %s" % (to, fro))
def isln(loc):
	Syn.log.l(Syn.log.PEDANTIC, "checking is similink path `%s'" % loc)
	return os.path.islink(loc)
def xists(loc):
	Syn.log.l(Syn.log.PEDANTIC, "checking path `%s'" % loc)
	return os.path.exists(loc)
def rmdir(dirs):
	Syn.log.l(Syn.log.PEDANTIC, "rmdir " + dirs)
	shutil.rmtree(dirs)
def rm(dirs):
	Syn.log.l(Syn.log.PEDANTIC, "rm " + dirs)
	os.remove(dirs)
def ln(source, dest):
	dirski = os.path.dirname(dest)
	if not xists(dirski):
		Syn.log.l(Syn.log.PEDANTIC, "Can't find it's basedir. Creating it")
		mkdir(dirski)
	Syn.log.l(Syn.log.PEDANTIC, "ln " + source + " to " + dest)
	os.symlink(source, dest)

