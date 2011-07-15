import Syn.json_bfile
import Syn.bfile
import hashlib
import os.path
import delt

#Remaking of the old verficiation md5sum function.
def md5sum(path):
	m = hashlib.md5()
	if path == '-':
		
		while True:
			d = sys.stdin.read(1024)
			if not d:
				break
			m.update(d)
		ret = m.hexdigest()
	else:
		try:
			pfile = file(path,'rb')
		except:
			return 'File open failed'
		while True:
			d = pfile.read(1024)
			if not d:
				break
			m.update(d)
		ret = m.hexdigest()
	return ret
#recursive function to go through file path and make md5sums of stuff thats not dirs
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

def makejsonbfile(filepath, file_id):

	ret = md5sumwd(filepath)
	jbfile = Syn.json_bfile.json_bfile(file_id)
	jbfile.setContent(ret)
	jbfile.write()
	
	return jbfile
#verifies that a dir and a json_bfile's contents are the same
def verify(filepath1,filepath2):

	
	try: 
		assert os.path.isdir(filepath2)
	except:
		print "Enter a file path in the second arg"
	try:
	
	 	assert type(filepath1) is Syn.json_bfile
	except:
		print "Enter a json_bfile for the first argument"

	file2 = makejsonbfile(filepath2,"file2")

	return delt.delt(filepath1.getContent(),file2.getContent())=={}



