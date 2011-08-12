#
# Because fuck you, that's why
#

MD5SUMFOLD=./meta/
MD5SUMFILE=$(MD5SUMFOLD)md5sum.mani

syn_patch:
	syn-helpers-patch

syn_strip_wd:
ifdef S_STRIP_BINARIES
	@echo "I: Stripping source"
	@cd $(S_DESTDIR) && syn-helpers-strip
else
	@echo "I: Not stripping source"
endif

syn_remove_blacklist:
	@echo "I: Removing blacklisted shaz."
	cd $(S_DESTDIR) && \
		rm -rf $(shell syn-plumbing get-build-blacklist)
