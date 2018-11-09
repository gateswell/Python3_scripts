#!/usr/bin/python
import os
import sys

num = {}
with open(sys.argv[1],'r') as fh:
	for line in fh:
		for i in range(len(line)):
			num[line[i]] = num.get(line[i],0) +1
base = ['A','C','G','T']
for alph in base:
	print(str(num[alph]),end = " ")