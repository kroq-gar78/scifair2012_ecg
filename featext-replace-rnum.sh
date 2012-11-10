for i in {101..103}; do sed -i "s/rnum\ \=\ '$((i-1))'/rnum\ \=\ '$i'/g" featExt.m; done
