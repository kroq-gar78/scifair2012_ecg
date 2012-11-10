for i in `find . -type d -not -path './.git*' -not -path './ECG_FEATURE_WAVELET_ST*' -not -name 'timestr' -not -name '.'|xargs`; do for j in p q r s t; do mv "${i:2}_$j.csv" $i; done; done
