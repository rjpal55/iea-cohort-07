#!/bin/bash
set -e

if [ "$#" = 0 ]; then
	echo "No arg given"
	exit 1
fi

for filein in "$@"; do
#	echo "$1 is first variable"
	if [[ ! -f ${filein} ]]; then
		echo "$filein doesn't exist"
	elif [[ -s ${filein} ]] ; then
		echo "inspected by RP" >> ${filein}
	else
		rm ${filein}
	fi
done
