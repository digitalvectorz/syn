# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import os
import Syn.policy.goodies as G

def get_files( dirpath):
	goodie_list=[]
	for member in os.listdir( dirpath):
		goodie_list.append(member)
	return goodie_list

def get_goodies():
	goodies={}
	#do binaries
	binaries=[]
	for b in G.BINARIES:
		for i in get_files(b):
			binaries.append(i)

	goodies["binaries"]=binaries
	#do lib	
	lib=[]

	for l in G.LIB:
		for j in get_files(l):
			lib.append(j)

	goodies["library"]=lib
	#do conf
	conf=[]

	
	for k in get_files(G.CONF):
		conf.append(k)

	goodies["conf"]=conf

	return goodies
