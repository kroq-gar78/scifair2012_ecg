#!/usr/bin/env python

import csv
import sys

# needed values from JBiSE:
# PR (probably PQ; P to (R or Q))
# QRS (Q to S)
# QT (Q to T)
# ST (S to T) - will require more work b/c uses diff endpoints from QT

rnum = int(sys.argv[1])

# this stuff is heart rate...
'''diffs = []
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
	rownum += 1'''

# translate the locations data into arrays

ploc = []
qloc = []
rloc = []
sloc = []
tloc = []

with open(str(rnum)+"/"+str(rnum)+"_p.csv",'rb') as f:
	pfile = csv.reader(f)
	for row in pfile:
		colnum = 0
		for col in row:
			if colnum != 0: continue
			ploc.append(int(col))
			colnum += 1

with open(str(rnum)+"/"+str(rnum)+"_q.csv",'rb') as f:
	qfile = csv.reader(f)
	for row in qfile:
		colnum = 0
		for col in row:
			if colnum != 0: continue
			qloc.append(int(col))
			colnum += 1

with open(str(rnum)+"/"+str(rnum)+"_r.csv",'rb') as f:
	rfile = csv.reader(f)
	for row in rfile:
		colnum = 0
		for col in row:
			if colnum != 0: continue
			rloc.append(int(col))
			colnum += 1

with open(str(rnum)+"/"+str(rnum)+"_s.csv",'rb') as f:
	sfile = csv.reader(f)
	for row in sfile:
		colnum = 0
		for col in row:
			if colnum != 0: continue
			sloc.append(int(col))
			colnum += 1

with open(str(rnum)+"/"+str(rnum)+"_t.csv",'rb') as f:
	tfile = csv.reader(f)
	for row in tfile:
		colnum = 0
		for col in row:
			if colnum != 0: continue
			tloc.append(int(col))
			colnum += 1

#qfile.close()

# check if there are an identical nubmer of each peak
if( not (len(ploc) == len(qloc)) and (len(qloc) == len(rloc)) and (len(rloc) == len(sloc)) and (len(sloc) == len(tloc))):
	print "ERROR: peak lists are not of the same size"
	exit(1)

# calculate QRS
qrslen = []
for i in xrange(len(qloc)):
	qrslen.append(sloc[i]-qloc[i])
#print qrslen

# calculate QT
qtlen = []
for i in xrange(len(qloc)):
	qtlen.append(tloc[i]-qloc[i])
#print qtlen

# calculate ST
stlen = []
for i in xrange(len(qloc)):
	stlen.append(tloc[i]-sloc[i])
#print stlen

# write segments to files
with open(str(rnum)+"/"+str(rnum)+"_qrs.csv",'wb') as f:
	qrswriter = csv.writer(f, dialect="excel")
	for i in xrange(len(qrslen)):
		qrswriter.writerow([qrslen[i]])

with open(str(rnum)+"/"+str(rnum)+"_qt.csv",'wb') as f:
	qtwriter = csv.writer(f, dialect="excel")
	for i in xrange(len(qtlen)):
		qtwriter.writerow([qtlen[i]])

with open(str(rnum)+"/"+str(rnum)+"_st.csv",'wb') as f:
	stwriter = csv.writer(f, dialect="excel")
	for i in xrange(len(stlen)):
		stwriter.writerow([stlen[i]])
