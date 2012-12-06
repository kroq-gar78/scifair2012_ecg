#!/usr/bin/env python

# Get the heart rate, average, maximum, and minimum QRS complex length

# TODO: min/max of all intervals, PR interval, max of P (relation to S? or max/min of all peaks)
# mas TODO: stdev of EVERYTHINGGG

# THE ORDER!
# RR, QRS, P, Q, R, S, T
# all min's, max's, avg's, stdev's

# AMMENDMENT: min/max/avg/stdev of QRS and RR - ONLY

import csv
import numpy as np
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
rintvlist = []
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
		rintvlist.append(tmplist)
		#rate = sum(tmplist)/len(tmplist)
		#rintv.append(rate)
		#rintv[rnum] = rate
#print rintv

# calculate averages, maximums, minumums, and standard deviations
# THE ORDER: min, max, avg, stdev
qrsavg = []
qrsmax = []
qrsmin = []
qrsstdev = []
rintvavg = []
rintvmax = []
rintvmin = []
rintvstdev = []
'''ratedata = []
qrsdata = []
pdata = []
qdata = []
rdata = []
sdata = []
tdata = []'''
for i in xrange(len(qrslist)):
	qrsavg.append(sum(qrslist[i])/len(qrslist[i]))
	qrsmax.append(max(qrslist[i]))
	qrsmin.append(min(qrslist[i]))
	qrsstdev.append(np.array(qrslist[i]).std())
	rintvavg.append(sum(rintvlist[i])/len(rintvlist[i]))
	rintvmax.append(max(rintvlist[i]))
	rintvmin.append(min(rintvlist[i]))
	rintvstdev.append(np.array(rintvlist[i]).std())

#for i in xrange(len(qrsavg)):
#	if(qrsavg[i]/360.0>0.14):
#		print ecglist[i]
#		if

# write all rates, avgs, maxs, mins to a single CSV
# qrsnn = QRS neural network (as in input to neural network)
with open('all_qrsnn.csv','wb') as f:
	qrsnnWriter = csv.writer(f, dialect="excel")
	for i in xrange(len(ecglist)):
		rnum = ecglist[i]
		#with open(str(rnum)+"/"+str(rnum)+"_qrsnn.csv",'wb') as f:
		qrsnnWriter.writerow([rnum,len(rintvlist),rintvavg[i],rintvstdev[i],rintvmax[i],rintvmin[i],qrsavg[i],qrsstdev[i],qrsmax[i],qrsmin[i]])
		'''rowdata = [rnum]
		rowdata.append(min(rintv))
		rowdata.append(max(rintv))
		rowdata.append(sum(rintv)/len(rintv))
		row
		for j in xrange(4):
			rowdata.append(sum(qrs[j])/len(qrs[j]))
		qrsnnWriter.writerow(rowdata)'''
		

# write another file with everything in seconds (versus samples)
with open('all_qrsnn_sec.csv','wb') as f:
	qrsnnSecWriter = csv.writer(f, dialect="excel")
	for i in xrange(len(ecglist)):
		rnum = ecglist[i]
		qrsnnSecWriter.writerow([rnum,len(rintvlist),rintvavg[i]/360.0,rintvstdev[i]/360.0,rintvmax[i]/360.0,rintvmin[i]/360.0,qrsavg[i]/360.0,qrsstdev[i]/360.0,qrsmax[i]/360.0,qrsmin[i]/360.0])
