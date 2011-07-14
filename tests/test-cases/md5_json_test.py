#!/usr/bin/env python
# Copyright 2011 (c) GNU GPL-3+, Ryan Maloney <rpm5779@rit.edu>

import Syn.md5_json
import os.path
import delt

test_dir=os.path.realpath("md5json")


test_dict={
	 "/home/ryan/syn/tests/md5json/iamadur/iamasubfile":"bf27e69237a4ad56e9589091c47bbc23",
	   "/home/ryan/syn/tests/md5json/iamafile1":"628bcee1e2cf5ae134866c5683631ff0",
	   "/home/ryan/syn/tests/md5json/iamafile2":"95ebe25eb6cc5ac8e2a2edcb339ca74b",
	   "/home/ryan/syn/tests/md5json/iamafile3":"58d5cb7865af03f2f7aeede04ef6acde"
	   }


result=Syn.md5_json.makejsonbfile(test_dir)
compare_content=result.getContent()

print compare_content

assert delt.delt(compare_content, test_dict) == {}


