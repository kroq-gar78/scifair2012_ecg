#!/usr/bin/env python

import csv

# needed values from JBiSE:
# PR (probably PQ; P to (R or Q))
# QRS (Q to S)
# QT (Q to T)
# ST (S to T) - will require more work b/c uses diff endpoints from QT

rnum = 100

# use "with open('filename') as f:" later on instead of this
pfile = csv.reader(open(str(rnum)+"/"+str(rnum)+"_p.csv",'rb'))
qfile = csv.reader(open(str(rnum)+"/"+str(rnum)+"_q.csv",'rb'))
rfile = csv.reader(open(str(rnum)+"/"+str(rnum)+"_r.csv",'rb'))
sfile = csv.reader(open(str(rnum)+"/"+str(rnum)+"_s.csv",'rb'))
tfile = csv.reader(open(str(rnum)+"/"+str(rnum)+"_t.csv",'rb'))

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

for row in pfile:
	colnum = 0
	for col in row:
		if colnum != 0: continue
		ploc.append(int(col))
		colnum += 1

for row in qfile:
	colnum = 0
	for col in row:
		if colnum != 0: continue
		qloc.append(int(col))
		colnum += 1
		
for row in rfile:
	colnum = 0
	for col in row:
		if colnum != 0: continue
		tloc.append(int(col))
		colnum += 1

for row in sfile:
	colnum = 0
	for col in row:
		if colnum != 0: continue
		sloc.append(int(col))
		colnum += 1
		
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
print qrslen

# calculate QT
qtlen = []
for i in xrange(len(qloc)):
	qtlen.append(tloc[i]-qloc[i])
print qtlen

# calculate ST
stlen = []
for i in xrange(len(qloc)):
	stlen.append(tloc[i]-sloc[i])
print stlen

'''print ploc
print qloc
print rloc
print sloc
print tloc'''
