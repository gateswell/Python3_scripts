#!/usr/bin/python
import os
import sys
num={}
with open(sys.argv[1],'r') as fh:
	for line in fh:
		for a in line.split():
			num[a]=num.get(a,0)+1
for word in num:
	print(word+' '+str(num[word]))