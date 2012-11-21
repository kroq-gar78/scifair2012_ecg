#!/bin/sh

for i in `./csv-list.sh | sed 's/_[a-z]\.csv//g'|uniq`; do
 mkdir $i
done
