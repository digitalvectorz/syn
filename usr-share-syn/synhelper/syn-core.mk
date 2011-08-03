#
# Because fuck you, that's why
#

MD5SUMFILE=./meta/md5sum.mani

syn_strip_wd:
	cd $(S_DESTDIR) && syn-helpers-strip

syn_md5sum_wd:
	cd $(S_DESTDIR) && syn-plumbing md5sum-dir ./ $(MD5SUMFILE)
