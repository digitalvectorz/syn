# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import Syn.json_bfile
import Syn.bfile
import hashlib
import os.path
import delt
import exceptions

def md5sum(path):
	m = hashlib.md5()
	try:
		pfile = file(path,'rb')
	except KeyError as e:
		raise Syn.exceptions.FileNotPresentException(str(e))
	while True:
		d = pfile.read(1024)
		if not d:
			break
		m.update(d)
	ret = m.hexdigest()
	return ret

def md5sumwd(check):
	ret = {}
	path = check

	for f in os.listdir(path):
		if os.path.isdir(path + "/" + f):
			dictret = md5sumwd(path + "/" + f)
			for x in dictret:
				ret[x] = dictret[x]
		elif os.path.islink(path + "/" + f):
			Syn.log.l(Syn.log.PEDANTIC, "similink not getting sum'd")
		else:
			Syn.log.l(Syn.log.PEDANTIC, "  " + path + "/" + f)
			ret[path + "/" + f] = md5sum(path + "/" + f)
	return ret

def makemd5sumfile(filepath, file_id):
	ret = md5sumwd(filepath)
	jbfile = Syn.json_bfile.json_bfile(file_id)
	jbfile.setContent(ret)
	jbfile.write()
	return jbfile

#verifies that a dir and a json_bfile's contents are the same
def verify(md5file, directory):	
	jbf = Syn.json_bfile.json_bfile(md5file)
	dhash = md5sumwd(directory)
	d = delt.delt( jbf.getContent(), dhash )
	return d

def md5sumfilematches(md5file, directory):
	delt = verify(md5file, directory)
	return delt == {}


