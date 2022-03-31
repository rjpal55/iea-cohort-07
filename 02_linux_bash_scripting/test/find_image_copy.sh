#!/bin/bash
find . -type f -exec file --mime-type {} \+ | awk -F: '{if ($2 ~/image\//) print $1}' | xargs cp '*' test/
