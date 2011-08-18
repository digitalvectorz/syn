"""
Get a list of all the binaries, libs, conf files and libs that
a package provides.

 @license: GPL-3+
 @author:  Ryan Maloney <rpm5779@rit.edu>
 @date:    August 6th, 2011, 01:50 -0000

 Get loads and loads of goodies. 
"""

import os.path
import Syn.Policy.Goodies as G
import Syn.Common

def getFiles( dirpath):
	"""
	XXX: Docme!
	@param dirpath: Explain me!
	@return: explain me!
	"""
	goodie_list=[]
	for member in os.listdir( dirpath):
		goodie_list.append(member)
	return goodie_list

def getGoodies( filepath ):
	"""
	XXX: Explain me!
	@param filepath: explain me!
	@return: explain me!
	"""
	
	goodie_list=[]
	if type(filepath) is list:
		for directory in filepath:
			goodies={}
			goodies[os.path.basename(directory)]=getFiles(directory)
			goodie_list.append(goodies)	
		return goodie_list	
	else:
		goodies={}
		goodies[os.path.basename(filepath)]=getFiles(filepath)
		goodie_list.append(goodies)
		return goodies
