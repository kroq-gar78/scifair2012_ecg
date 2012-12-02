#!/bin/sh

# symlink to all of the necessary files in a new directory (e.g. for a new filter)

strend=m.*

# symlink all matlab records
for i in `find ../ -maxdepth 1 -name '*.mat'|grep -e "[0-9][0-9][0-9]m\.mat"|sed 's/m\.mat//g'|sed 's/\.\.\///g'|sort`; do
    ln -s ../$i$strend .
done

# symlink all other scripts/programs except "featExt.m"
for i in mk-ecg-dirs.sh mat-mv-to-dirs.sh mat2csv.py qrsCalc.py qrsCombine.py featext-automated.sh featext-matlab-cli.sh csv-list.sh csv-mv-to-dirs.sh librow_winmax.m find-ecg-dirs.sh find-ecgs.sh mat2csv.sh qrsCalc.sh do-everything.sh; do
    ln -s ../$i .
done

# copy instead of symlink "featExt.m" because it is modified during the run
cp -va ../featExt.m ./
