#!/usr/bin/env python

import csv

# needed values from JBiSE:
# PR (probably PQ; P to (R or Q))
# QRS (Q to S)
# QT (Q to T)
# ST (S to T)

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

print ploc
print qloc
print rloc
print sloc
print tloc
