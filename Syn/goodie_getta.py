# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import os.path
import Syn.policy.goodies as G
import Syn.common

def get_files( dirpath):
	goodie_list=[]
	for member in os.listdir( dirpath):
		goodie_list.append(member)
	return goodie_list

def get_goodies( filepath ):
	
	goodie_list=[]
	if type(filepath) is list:
		for directory in filepath:
			goodies={}
			goodies[os.path.basename(directory)]=get_files(directory)
			goodie_list.append(goodies)	
		return goodie_list	
	else:
		goodies={}
		goodies[os.path.basename(filepath)]=get_files(filepath)
		goodie_list.append(goodies)
		return goodies
