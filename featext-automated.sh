#/bin/bash -eu
records=`find . -maxdepth 1 -name '*.mat'|grep -e "[0-9][0-9][0-9]m\.mat"|sed 's/m\.mat//g'|sed 's/\.\///g'|sort`
for i in `echo $records|xargs`; do
	echo $i
	sed -i "s/rnum\ \=\ '[0-9][0-9][0-9]'/rnum\ \=\ '$i'/g" featExt.m
	matlab -glnx86 -r "path(path,'.'); featExt; exit" -nodesktop -nosplash
done
