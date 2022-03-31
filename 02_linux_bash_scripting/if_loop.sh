#!/bin/bash
if test ! -f "$@"; then
	echo "$@ doesn't exist"
fi
