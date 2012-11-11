#/bin/bash -eu
records=`find . -type d -not -path './.git*' -not -path './ECG_FEATURE_WAVELET_ST*' -not -name 'timestr' -not -name '.'|sort`
for i in `echo $records|xargs`; do
	rnum=${i:2}
	sed -i "s/rnum\ \=\ '[0-9][0-9][0-9]'/rnum\ \=\ '$rnum'/g" featExt.m
	matlab -glnx86 -r "path(path,'.'); featExt; exit" -nodesktop -nosplash
done
