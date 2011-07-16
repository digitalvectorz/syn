#!/usr/bin/env python

from distutils.core import setup

setup(
	name       = 'syn',
	version    = '3.0',
	packages   = [ 'Syn', 'Syn.policy' ],
	data_files = [
		('/usr/share/syn/synd-template', [
			'usr-share-syn/synd-template/build',
			'usr-share-syn/synd-template/build.env',
			'usr-share-syn/synd-template/metapkg',
		])
	]
)
