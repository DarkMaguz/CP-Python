#!/bin/sh -e

SCRIPT_PATH=`dirname $(readlink -f $0)`
UPDATE_FILES=$SCRIPT_PATH/update_*.sh

TIMESTAMP_FILE=$SCRIPT_PATH/timestamp

if [ ! -e $TIMESTAMP_FILE ]; then
	echo "2017-01-01"> $TIMESTAMP_FILE
fi

TODAY=$(date +%s)
LAST_CHECK=$(date -d $(cat $TIMESTAMP_FILE) +%s)

DAYS_SINCE_LAST_UPDATE=$((($TODAY - $LAST_CHECK)/60/60/24))

if [ $DAYS_SINCE_LAST_UPDATE -gt 0 ]; then
	echo "Checking for updates..."
	for UPDATE_FILE in $UPDATE_FILES; do
		sh $UPDATE_FILE
	done
	date --iso-8601> $TIMESTAMP_FILE
else
	echo "Last checked for updates less than 24 hours ago."
fi

