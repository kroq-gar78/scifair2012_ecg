#!/usr/bin/env python

import csv

rnum = 100

rfile = csv.reader(open(str(rnum)+"/"+str(rnum)+"_r.csv",'rb'))
pfile = csv.reader(open(str(rnum)+"/"+str(rnum)+"_p.csv",'rb'))
qfile = csv.reader(open(str(rnum)+"/"+str(rnum)+"_q.csv",'rb'))
sfile = csv.reader(open(str(rnum)+"/"+str(rnum)+"_s.csv",'rb'))
tfile = csv.reader(open(str(rnum)+"/"+str(rnum)+"_t.csv",'rb'))

diffs = []
rownum = 0
prevq = 0
curq = 0
for row in rfile:
	colnum = 0
	for col in row:
		#print col
		if colnum != 0: continue
		if rownum > 0:
			prevq = curq
			#print col
			curq = int(col)
			diffs.append(int(curq-prevq))
		else:
			curq = float(col)
			print "done"
		colnum += 1
	rownum += 1

#qfile.close()

print diffs
