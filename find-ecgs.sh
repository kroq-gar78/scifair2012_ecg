#!/bin/bash
for i in `find . -maxdepth 1 -name '*.csv'|grep -e "[0-9][0-9][0-9]\.csv"|sed 's/\.csv//g'|sed 's/\.\///g'|sort`; do
	echo $i
done
