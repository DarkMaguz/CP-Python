#!/bin/sh -e

cd `dirname $(readlink -f $0)`

LATEST_VERSION=$(wget --spider -S --max-redirect 0 "https://github.com/mozilla/geckodriver/releases/latest" 2>&1 | grep "Location:" -m 1 | rev | cut -d/ -f1 | rev | cut -dv -f2)

if [ -x "geckodriver" ]; then
	CURRENT_VERSION=$(./geckodriver --version 2>&1 | sed -n 1p | cut -d' ' -f2)
else
	CURRENT_VERSION="0.0.0"
fi

if [ "$LATEST_VERSION" != "$CURRENT_VERSION" ]; then
	echo "Found an outdated version of geckodriver \"$CURRENT_VERSION\"."
	echo "Downloading lates version of geckodriver \"$LATEST_VERSION\"."
	rm -f geckodriver
	wget "https://github.com/mozilla/geckodriver/releases/download/v$LATEST_VERSION/geckodriver-v$LATEST_VERSION-linux64.tar.gz"
	tar -xvf "geckodriver-v$LATEST_VERSION-linux64.tar.gz"
	rm -f "geckodriver-v$LATEST_VERSION-linux64.tar.gz"
else
	echo "geckodriver is up to date: \"$LATEST_VERSION\""
fi
