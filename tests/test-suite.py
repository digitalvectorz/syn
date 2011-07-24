#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Paul Tagliamonte <paultag@gmail.com>

import os.path
import sys
import unittest

folder = os.path.dirname(os.path.abspath(__file__)) + "/unittests"

sys.path.append(folder)
to_import = [f for f in os.listdir(folder) if not f.endswith(".pyc")]

for mod in to_import:
	if mod.endswith(".py"):
		name = mod [:-3]
		__import__(name)

if __name__ == "__main__":
            unittest.main()
