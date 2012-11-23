#!/usr/bin/env python

# Get the heart rate, average, maximum, and minimum QRS complex length

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

# calculate heart rate (R peak to R peak interval) after reading
rintv = []
for rnum in ecglist:
	with open(str(rnum)+"/"+str(rnum)+"_r.csv",'rb') as f:
		tmpcsv = csv.reader(f)
		# read
		rlist = []
		for row in tmpcsv:
			rlist.append(int(row[0]))
		#print rlist
		# calculate
		tmplist = []
		for j in xrange(len(rlist)-1):
			#print rlist[j+1],rlist[i]
			tmplist.append(rlist[j+1]-rlist[j])
		#rintv.append(tmplist)
		rate = sum(tmplist)/len(tmplist)
		rintv.append(rate)
		#rintv[rnum] = rate
#print rintv

# calculate averages, maximums, and minimums
qrsavg = []
qrsmax = []
qrsmin = []
for i in xrange(len(qrslist)):
	qrsavg.append(sum(qrslist[i])/len(qrslist[i]))
	qrsmax.append(max(qrslist[i]))
	qrsmin.append(min(qrslist[i]))

# write all rates, avgs, maxs, mins to a single CSV
# qrsnn = QRS neural network (as in input to neural network)
with open('all_qrsnn.csv','wb') as f:
	qrsnnWriter = csv.writer(f, dialect="excel")
	for i in xrange(len(ecglist)):
		rnum = ecglist[i]
		#with open(str(rnum)+"/"+str(rnum)+"_qrsnn.csv",'wb') as f:
		qrsnnWriter.writerow([rnum,rintv[i],qrsavg[i],qrsmax[i],qrsmin[i]])
