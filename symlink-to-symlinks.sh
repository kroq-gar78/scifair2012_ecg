#!/bin/sh

strend=m.*

for i in `find ../ -maxdepth 1 -name '*.mat'|grep -e "[0-9][0-9][0-9]m\.mat"|sed 's/m\.mat//g'|sed 's/\.\.\///g'|sort`; do
    ln -s ../$i$strend .
done
