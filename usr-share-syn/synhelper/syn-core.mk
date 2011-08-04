#
# Because fuck you, that's why
#

MD5SUMFOLD=./meta/
MD5SUMFILE=$(MD5SUMFOLD)md5sum.mani

syn_strip_wd:
ifdef S_STRIP_BINARIES
	@echo "I: Stripping source"
	@cd $(S_DESTDIR) && syn-helpers-strip
else
	@echo "I: Not stripping source"
endif
