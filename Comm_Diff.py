#!/usr/bin/env python
import sys
import os
import re

num ={}
hash ={}

with open(sys.argv[1]) as fh1:
	lines = fh1.readlines()
	for line in lines:
		tmp = line.split('\t')
		pos = '|'.join(tmp[i] for i in [0,1,2,4]).rstrip()
		num[pos] = 0
		num[pos] += 1
		#hash[str(sys.argv[1])][pos] = line
		hash[pos] = line

with open(sys.argv[2]) as fh2:
	lines2 = fh2.readlines()
	for line2 in lines2:
		string = line2.split('\t')
		pos2 = '|'.join(string[i] for i in [0,1,2,-1]).rstrip()
		if pos2 in num.keys():
			num[pos2] = 3
		else:
			num[pos2] = 2
		#hash[str(sys.argv[2])][pos2] = line2
		hash[pos2] = line2

name1 = re.search(r"(.*\\)(\w+)\.txt$",sys.argv[1])
#print(name1.group(1))
name2 = re.search(r"(.*\\)(\w+)\.txt$",sys.argv[2])

fo1 = open(name1.group(1) + name1.group(2) + '_spec.txt','w')
fo2 = open(name1.group(1) + name2.group(2) + '_spec.txt','w')
fo3 = open(name1.group(1) + name1.group(2) + '_' + name2.group(2) + '_comm.txt','w')
for posi,value in num.items():
	if int(value) ==1:
		fo1.write(hash[posi])
	elif int(value) ==2:
		fo2.write(hash[posi])
	elif int(value) ==3:
		fo3.write(hash[posi])