#!/bin/sh

for i in `./find-ecg-dirs.sh |xargs`; do
	cd $i
	for j in *.csv; do
		echo $j
	done
	cd ../
done
