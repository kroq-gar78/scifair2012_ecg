for i in `find . -maxdepth 1 -type f -name '*.csv'|sed 's/\.\///g' |sort|xargs`; do
	directory=`echo $i|sed 's/_[a-z]\.csv//g'`
	if [ ! -e $directory ]; then mkdir $directory; fi
	mv $i $directory
done
