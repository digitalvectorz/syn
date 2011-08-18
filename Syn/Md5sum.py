"""
Simple md5sum type stuffs.

 @license: GPL-3+
 @author:  Ryan Maloney <rpm5779@rit.edu>
 @date:    August 6th, 2011, 01:50 -0000

 Do MD5-summing
"""

from pprint import pprint

import Syn.JsonBfile
import Syn.Bfile
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
		raise Syn.Exceptions.FileNotPresentException(str(e))
	while True:
		d = pfile.read(1024)
		if not d:
			break
		m.update(d)
	ret = m.hexdigest()
	return ret

def hashWorkingDir(path):
	"""
	XXX: Explain me!
	@param path: explain me!
	@return: explain me
	"""
	ret = {}

	for f in os.listdir(path):
		if os.path.isdir(path + "/" + f):
			dictret = hashWorkingDir(path + "/" + f)
			for x in dictret:
				ret[x] = dictret[x]
		elif os.path.islink(path + "/" + f):
			Syn.Log.l(Syn.Log.PEDANTIC, "similink not getting sum'd")
		else:
			Syn.Log.l(Syn.Log.PEDANTIC, "  " + path + "/" + f)
			ret[path + "/" + f] = md5sum(path + "/" + f)
	return ret

def createMd5HashFile(filepath, file_id):
	"""
	XXX: Explain me!
	@param filepath: explain me
	@param file_id:  explain me
	@return: explain me
	"""
	ret = hashWorkingDir(filepath)
	jbfile = Syn.JsonBfile.JsonBfile(file_id)
	jbfile.setContent(ret)
	jbfile.write()
	return jbfile

#verifies that a dir and a JsonBfile's contents are the same
## XXX Obsolete??
def verify(md5file, darg):
	"""
	XXX: Explain me!
	@param md5file: explain me
	@param darg: explain me
	@return: explain me
	"""
	jbf = Syn.JsonBfile.JsonBfile(md5file)
	dhash = darg

	if not Syn.Common.isdict(darg):  # argument passed is NOT of type dict
		dhash = hashWorkingDir(darg)
	
	d = Syn.Common.delt( jbf.getContent(), dhash )
	return d

def md5FileCheck(md5file, directory):
	"""
	XXX: Explain me!
	@param md5file: explain me
	@param directory: explain me
	@return: explain me
	"""
	delt = verify(md5file, directory)
	return delt == {}


