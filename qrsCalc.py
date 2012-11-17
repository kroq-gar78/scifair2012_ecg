#!/usr/bin/env python

import csv

rnum = 100

qfile = csv.reader(open(str(rnum)+"/"+str(rnum)+"_q.csv",'rb'))

diffs = []
rownum = 0
prevq = 0
curq = 0
for row in qfile:
	colnum = 0
	for col in row:
		#print col
		if colnum != 0: continue
		if rownum > 0:
			prevq = curq
			#print col
			try:
				curq = float(col)
			except:
				curq = 0
			diffs.append(int(curq-prevq))
		else:
			curq = float(col)
			print "done"
		colnum += 1
	rownum += 1

#qfile.close()

print diffs
