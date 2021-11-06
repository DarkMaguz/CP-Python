#!/bin/sh -e

cd `dirname $(readlink -f $0)`

LATEST_VERSION=$(wget --spider -S --max-redirect 0 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=da" 2>&1 | sed -n '/Location: /{s|.*/firefox-\(.*\)\.tar.*|\1|p;q;}')

if [ -e ./firefox/application.ini ]; then
	CURRENT_VERSION=$(sed -n -e 's/^\s*Version\s*=\s*//p' ./firefox/application.ini)
else
	CURRENT_VERSION="0.0.0"
fi

if [ "$LATEST_VERSION" != "$CURRENT_VERSION" ]; then
	echo "Found an outdated version of firefox \"$CURRENT_VERSION\"."
	echo "Downloading lates version of firefox \"$LATEST_VERSION\"."
	rm -rf firefox/
	wget $(wget --spider -S --max-redirect 0 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=da" 2>&1 | grep "Location:" - | cut -d' ' -f4)
	FIREFOX_BIN_ARCHIVE=$(wget --spider -S --max-redirect 0 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=da" 2>&1 | grep "Location:" -m 1 | rev | cut -d/ -f1 | rev)
	tar -xvf $FIREFOX_BIN_ARCHIVE
	rm -f $FIREFOX_BIN_ARCHIVE
else
	echo "Firefox is up to date: \"$CURRENT_VERSION\""
fi

