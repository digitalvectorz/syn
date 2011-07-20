Syn Package Manager
=====================

Hi. This is Syn. Syn's a package manager. It's written in Python, and focused on modern, compact and minimal design. It does what it should, and it gets out of your way. Tons of concepts were shamlessly taken from Debian's dpkg, but with a few modern twists. 

Syn is not for people who want something stable and time tested, dpkg is a much better choice for that. Syn's devlopers love building things up from scratch, so feel free to use Syn how you see fit. Syn's flagship Distro, Synnamon, is not yet ready for use. There's a lot to consider. 

As always, patches are more then welcome (they're encouraged), and will be rewarded with good tidings from the Developers. If you plan to send a pull request or a format-patch, please rebase and squash all commits into logical chunks.

Syn is GNU GPL Free and Open source. Authors can be found in the AUTHORS file.

To get a full list of all commiters (this is messy):

$ git log | grep Author | sort | uniq | sed s/Author:\ //g
