#!/bin/bash
if [ -z $@ ]; then
	echo "No arg given"
fi

for filein in "$@"; do
#	echo "$1 is first variable"
	if [ ! -f $filein ]; then
		echo "$filein doesn't exist"
	elif [ -f $filein ] ; then
		echo "inspected by RP" >> $filein
	fi
done

