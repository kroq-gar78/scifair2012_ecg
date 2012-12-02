#!/bin/sh

# automatically runs 'mat2csv.py' for all ECG's

for i in `./find-ecgs.sh`; do
    python mat2csv.py $i
done
