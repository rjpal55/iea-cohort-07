#!/bin/bash
find -maxdepth 1 -name '*.txt' | xargs ls | wc -l
