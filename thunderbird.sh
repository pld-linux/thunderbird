#!/bin/sh
# based on script by (c) vip at linux.pl, wolf at pld-linux.org

LIBDIR="@LIBDIR@/thunderbird"

# copy profile from Icedove if its available and if no Thunderbird
# profile exists
if [ ! -d $HOME/.thunderbird ] && [ -d $HOME/.icedove ]; then
	echo "Copying profile from Icedove"
	cp -a $HOME/.icedove $HOME/.thunderbird
fi

# compreg.dat and/or chrome.rdf will screw things up if it's from an
# older version. http://bugs.gentoo.org/show_bug.cgi?id=63999
for f in ~/.thunderbird/*/{compreg.dat,chrome.rdf,XUL.mfasl}; do
	[ -f "$f" ] || continue
	if [ "$f" -ot "$0" ] || [ "$f" -ot "$LIBDIR/components/compreg.dat" ]; then
		echo "Removing $f leftover from older Thunderbird"
		rm -f "$f"
	fi
done

THUNDERBIRD="$LIBDIR/thunderbird"

exec $THUNDERBIRD "$@"
