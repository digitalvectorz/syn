#!/usr/bin/env python

from Syn import __appname__, __version__

import os
from os.path import join
from distutils.core import setup

KEY_PFIX = "/usr/share/syn/"

def fucking_recusion_how_does_it_work_not_here():
	ret = []
	for root, dirs, files in os.walk('usr-share-syn'):
		if files != []:
			inst_pfix = KEY_PFIX + os.path.basename(root)
			frobernate = []
			for f in files:
				frobernate.append(root + "/" + f)
			val = ( inst_pfix, frobernate )
			ret.append(val)
	return ret

usrshare = fucking_recusion_how_does_it_work_not_here()
print usrshare

setup(
	name       = __appname__,
	version    = __version__,
	packages   = [ 'Syn', 'Syn.policy' ],
	data_files = usrshare
)
