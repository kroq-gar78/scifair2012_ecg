#!/bin/bash
for i in `find . -maxdepth 1 -name '*.mat'|grep -e "[0-9][0-9][0-9]m\.mat"|sed 's/m\.mat//g'|sed 's/\.\///g'|sort`; do
	echo $i
done
