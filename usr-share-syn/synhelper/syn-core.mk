#
# Because fuck you, that's why
#

MD5SUMFILE=./md5sum.mani

syn_strip_wd:
	syn-helpers-strip

syn_md5sum_wd:
	syn-plumbing md5sum-dir $(MD5SUMFILE) ./
