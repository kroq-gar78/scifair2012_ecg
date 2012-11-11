#/bin/bash -eu
rlength=$((`find . -type d -not -path './.git*' -not -path './ECG_FEATURE_WAVELET_ST*' -not -name 'timestr' -not -name '.'|wc -l`))
records=`find . -type d -not -path './.git*' -not -path './ECG_FEATURE_WAVELET_ST*' -not -name 'timestr' -not -name '.'|sort`
#for i in `echo $records|xargs`; do
for (( i = 2; i <= $rlength; i+=1)); do
	rnum=`echo $records| cut -d" " -f$i`
	rnum=${rnum:2}
	rnum_old=`echo $records| cut -d" " -f$((i-1))`
	rnum_old=${rnum_old:2}
	sed -i "s/rnum\ \=\ '$rnum_old'/rnum\ \=\ '$rnum'/g" featExt.m
	matlab -glnx86 -r "path(path,'.'); featExt; exit" -nodesktop -nosplash
done
