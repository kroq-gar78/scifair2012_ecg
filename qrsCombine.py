#!/usr/bin/env python

# Get the average, maximum, and minimum QRS complex length

import csv
import subprocess # for system commands
#import os

# get the list of ECG's that work

p = subprocess.Popen('./find-ecg-dirs.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
ecglist = []
for i in p.stdout.readlines():
	ecglist.append(int(i))
#print ecglist

# read all of the points from each CSV file (suffix "_qrs.csv")
qrslist = []
for rnum in ecglist:
	with open(str(rnum)+"/"+str(rnum)+"_qrs.csv",'rb') as f:
		tmpcsv = csv.reader(f)
		tmplist = []
		for row in tmpcsv:
			tmplist.append(int(row[0]))
		qrslist.append(tmplist)

# calculate averages
qrsavg = []
for i in xrange(len(qrslist)):
	qrsavg.append(sum(qrslist[i])/sum(qrslist[i]))

# calculate maximums
qrsmax = []
for i in xrange(len(qrslist)):
	qrsmax.append(max(qrslist[i]))

# calculate minimums
qrsmin = []
for i in xrange(len(qrslist)):
	qrsmin.append(min(qrslist[i]))
