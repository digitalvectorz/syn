#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import Syn.sh
import Syn.synd

Syn.sh.cd("test-builder")
Syn.synd.build("bash-4.2.syn.tar.gz")
