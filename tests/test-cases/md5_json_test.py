#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import Syn.md5sum
import Syn.common
import os.path
import delt

cur_dir = Syn.common.getcwd()


test_dir = os.path.relpath("md5json",cur_dir)
<<<<<<< HEAD
#test_dir2 = os.path.relpath("md5json2",cur_dir)
=======
test_dir2 = os.path.relpath("md5json2",cur_dir)
>>>>>>> 0cf8cf0feadb170edf657398b999a3207febb6f3

test_dict = {
	"md5json/iamadur/iamasubfile"  : "bf27e69237a4ad56e9589091c47bbc23",
	"md5json/iamafile1"            : "628bcee1e2cf5ae134866c5683631ff0",
	"md5json/iamafile2"            : "95ebe25eb6cc5ac8e2a2edcb339ca74b",
	"md5json/iamafile3"            : "58d5cb7865af03f2f7aeede04ef6acde"
}

result = Syn.md5sum.makejsonbfile(test_dir)
compare_content = result.getContent()

assert delt.delt(compare_content, test_dict) == {}

assert Syn.md5sum.verify(result,test_dir)
<<<<<<< HEAD

test_dir2 = os.path.relpath("synd",cur_dir)

assert Syn.md5sum.verify(result,test_dir2)==False
=======
>>>>>>> 0cf8cf0feadb170edf657398b999a3207febb6f3
