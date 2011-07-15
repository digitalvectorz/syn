# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.policy.source_package as S
import Syn.exceptions
import Syn.json_file
import Syn.common
import Syn.log

def loadEnv():
	envfile = S.SOURCE_DIRECTORY + "/" + S.ENVFILE
	env = Syn.json_file.json_file(envfile)
	envdict = env.getContent()
	for x in S.BUILD_ENV_KEYS:
		try:
			val = envdict[x]
		except KeyError as e:
			Syn.log.l(Syn.log.CRITICAL,"Oh shit. Env key missing: %s" % e)
			raise Syn.exceptions.SynFormatException(str(e))

		if type(val) == list:
			combined_val = ""
			for y in envdict[x]:
				combined_val += y
			Syn.common.putenv(x, combined_val)
		else:
			Syn.common.putenv(x, val)
