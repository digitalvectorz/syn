#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.plumbing.build_package
import Syn.exceptions
import Syn.log

try:
	Syn.plumbing.build_package.run(None)
except Syn.exceptions.SynFormatException as e:
	Syn.log.l(Syn.log.CRITICAL,"SE: %s" % str(e))
