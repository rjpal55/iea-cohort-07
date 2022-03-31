#!/bin/bash
if [ -z "$@" ]; then
	echo "No arg given"
elif [ ! -f "$@" ]; then
	echo "$@ doesn't exist"
fi
