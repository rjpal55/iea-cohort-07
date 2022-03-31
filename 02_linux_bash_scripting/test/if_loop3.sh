#!/bin/bash
for filein in "$@"; do
	echo "$1 is first variable"
	if [ -z $filein ]; then
		echo "No arg given"
	elif [ ! -f $filein ]; then
		echo "$filein doesn't exist"
	fi
done

