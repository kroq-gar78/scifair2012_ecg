#!/bin/sh -eu

# automatically runs 'qrsCalc.py' for all ECG's
# all ECG's must be in directories by this point

for i in `./find-ecg-dirs.sh`; do
    python qrsCalc.py $i
done
