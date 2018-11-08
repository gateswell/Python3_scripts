#!/usr/bin/python
import os
import sys

num = 0
with open(sys.argv[1],'r') as fh:
	for line in fh:
		num +=1
		if not num %2:
			print(line.rstrip())