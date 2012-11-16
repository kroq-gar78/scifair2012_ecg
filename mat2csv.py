#!/usr/bin/env python

# Convert .mat files into .csv files

import csv
import scipy.io

# test conversion with 1 ECG file first

rnum = 100

# read the .mat file
mat = scipy.io.loadmat(str(rnum)+'_r.mat')
vals = []
#for i in mat['Rloc']:
#	vals[0].append(int(i))
#for i in mat['Ramp']:
#	vals[1].append(int(i))

for i in xrange(len(mat['Rloc'])):
	vals.append([int(mat['Rloc'][i]),int(mat['Ramp'][i])])

print vals

# write the data into a .csv file
rfile = open((str(rnum)+"_r.csv"),'wb')
rwriter = csv.writer(rfile, dialect="excel")

for i in vals:
	rwriter.writerow([i[0],i[1]])

rfile.close()
