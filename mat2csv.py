#!/usr/bin/env python

# Convert .mat files into .csv files

import csv
import scipy.io
import sys

# test conversion with 1 ECG file first

rnum = int(sys.argv[1])

# read the .mat files
matr = scipy.io.loadmat(str(rnum)+'_r.mat')
matp = scipy.io.loadmat(str(rnum)+'_p.mat')
matq = scipy.io.loadmat(str(rnum)+'_q.mat')
mats = scipy.io.loadmat(str(rnum)+'_s.mat')
matt = scipy.io.loadmat(str(rnum)+'_t.mat')

#for i in mat['Rloc']:
#	vals[0].append(int(i))
#for i in mat['Ramp']:
#	vals[1].append(int(i))

# write the data into a .csv file
rfile = open((str(rnum)+"_r.csv"),'wb')
pfile = open((str(rnum)+"_p.csv"),'wb')
qfile = open((str(rnum)+"_q.csv"),'wb')
sfile = open((str(rnum)+"_s.csv"),'wb')
tfile = open((str(rnum)+"_t.csv"),'wb')
rwriter = csv.writer(rfile, dialect="excel")
pwriter = csv.writer(pfile, dialect="excel")
qwriter = csv.writer(qfile, dialect="excel")
swriter = csv.writer(sfile, dialect="excel")
twriter = csv.writer(tfile, dialect="excel")

for i in xrange(len(matr['Rloc'])):
	rwriter.writerow([int(matr['Rloc'][i]),int(matr['Ramp'][i])])
for i in xrange(len(matp['Ploc'])):
	pwriter.writerow([int(matp['Ploc'][i]),int(matp['Pamp'][i])])
for i in xrange(len(matq['Qloc'])):
	qwriter.writerow([int(matq['Qloc'][i]),int(matq['Qamp'][i])])
for i in xrange(len(mats['Sloc'])):
	swriter.writerow([int(mats['Sloc'][i]),int(mats['Samp'][i])])
for i in xrange(len(matt['Tloc'])):
	twriter.writerow([int(matt['Tloc'][i]),int(matt['Tamp'][i])])

rfile.close()
pfile.close()
qfile.close()
sfile.close()
tfile.close()
