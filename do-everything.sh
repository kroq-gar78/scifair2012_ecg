#!/bin/sh -eu

# do everything for one run

./featext-automated.sh
./mat2csv.sh
./mk-ecg-dirs.sh
./mat-mv-to-dirs.sh
./csv-mv-to-dirs.sh
./qrsCalc.sh
python qrsCombine.py
