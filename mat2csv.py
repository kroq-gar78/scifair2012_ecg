#!/usr/bin/env python

# Convert .mat files into .csv files

import csv
import scipy.io

# test conversion with 1 ECG file first

rnum = 100

# read the .mat file
mat = scipy.io.loadmat(str(rnum)+'_r.mat')

#for i in mat['Rloc']:
#	vals[0].append(int(i))
#for i in mat['Ramp']:
#	vals[1].append(int(i))

print vals

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

for i in xrange(len(mat['Rloc'])):
	rwriter.writerow([int(mat['Rloc'][i]),int(mat['Ramp'][i])])
for i in xrange(len(mat['Ploc'])):
	pwriter.writerow([int(mat['Ploc'][i]),int(mat['Pamp'][i])])
for i in xrange(len(mat['Qloc'])):
	qwriter.writerow([int(mat['Qloc'][i]),int(mat['Qamp'][i])])
for i in xrange(len(mat['Sloc'])):
	swriter.writerow([int(mat['Sloc'][i]),int(mat['Samp'][i])])
for i in xrange(len(mat['Tloc'])):
	rwriter.writerow([int(mat['Tloc'][i]),int(mat['Tamp'][i])])

rfile.close()
