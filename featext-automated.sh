#/bin/bash -eu
records=`./find-ecgs.sh`
for i in `echo $records|xargs`; do
	echo $i
	sed -i "s/rnum\ \=\ '[0-9][0-9][0-9]'/rnum\ \=\ '$i'/g" featExt.m
	matlab -glnx86 -r "path(path,'.'); featExt; exit" -nodesktop -nosplash
done
