#
# Ohai!
#

include /usr/share/syn/synhelper/syn-core.mk

cfg:
	$(S_CONFIGURE) $(S_CONFIGURE_FLAGS)
build:
	$(S_BUILD) $(S_BUILD_FLAGS)
stage:
	$(S_STAGE) DESTDIR=$(S_DESTDIR) $(S_STAGE_FLAGS)
