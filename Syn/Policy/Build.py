#

FOLDER_BLACKLIST = [
	# Blacklist shittyisms here.
	"usr/share/info"  # This is just such a stupid design.
]

BUILD_PROCESS = [
	"syn_patch",
	"cfg",
	"build",
	"stage",
	"syn_remove_blacklist",
	"syn_strip_wd",
]
