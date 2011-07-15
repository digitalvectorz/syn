import Syn.json_bfile
import Syn.bfile
import hashlib
import os.path


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

def makejsonbfile(filepath):
	
	file_id = "json_bfile-testjson.testdb"
	ret = md5sumwd(filepath)
	jbfile = Syn.json_bfile.json_bfile(file_id)
	jbfile.setContent(ret)
	jbfile.write()
	
	return jbfile
