"""
Simple md5sum type stuffs.

 @license: GPL-3+
 @author:  Ryan Maloney <rpm5779@rit.edu>
 @date:    August 6th, 2011, 01:50 -0000

 Do MD5-summing
"""

from pprint import pprint

import Syn.json_bfile
import Syn.bfile
import hashlib
import os.path
import exceptions

def md5sum(path):
	"""
	XXX: Explain me!
	@param path: Explain me!
	"""
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

def md5sumwd(path):
	"""
	XXX: Explain me!
	@param path: explain me!
	@return: explain me
	"""
	ret = {}

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
	"""
	XXX: Explain me!
	@param filepath: explain me
	@param file_id:  explain me
	@return: explain me
	"""
	ret = md5sumwd(filepath)
	jbfile = Syn.json_bfile.json_bfile(file_id)
	jbfile.setContent(ret)
	jbfile.write()
	return jbfile

#verifies that a dir and a json_bfile's contents are the same
def verify(md5file, darg):
	"""
	XXX: Explain me!
	@param md5file: explain me
	@param darg: explain me
	@return: explain me
	"""
	jbf = Syn.json_bfile.json_bfile(md5file)
	dhash = darg

	if not Syn.common.isdict(darg):  # argument passed is NOT of type dict
		dhash = md5sumwd(darg)
	
	d = Syn.common.delt( jbf.getContent(), dhash )
	return d

def md5sumfilematches(md5file, directory):
	"""
	XXX: Explain me!
	@param md5file: explain me
	@param directory: explain me
	@return: explain me
	"""
	delt = verify(md5file, directory)
	return delt == {}


