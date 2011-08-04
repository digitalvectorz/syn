#
# Because fuck you, that's why
#

MD5SUMFOLD=./meta/
MD5SUMFILE=$(MD5SUMFOLD)md5sum.mani

syn_strip_wd:
	cd $(S_DESTDIR) && syn-helpers-strip

syn_md5sum_wd:
	mkdir $(S_BINARY_ROOT)$(MD5SUMFOLD)
	cd $(S_BINARY_ROOT) && syn-plumbing md5sum-dir ./ $(MD5SUMFILE)
