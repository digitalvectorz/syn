#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import Syn.goodie_getta as getta

test=getta.get_goodies(["/usr/bin","/etc"])
test2=getta.get_goodies("/usr/bin")


assert len(test2)==1

assert len(test)==2

assert test[0].has_key("bin")

assert test[1].has_key("etc")

assert test2.has_key("bin")
