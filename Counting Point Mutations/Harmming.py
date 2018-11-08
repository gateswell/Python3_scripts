#!/usr/bin/python
import os
import sys

harmming = 0
with open(sys.argv[1],'r') as fh:
	line1 = fh.readline().rstrip()
	line2 = fh.readline().rstrip()
	for i in range(len(line1)):
		if line1[i] == line2[i]:
			harmming += 0
		else:
			harmming += 1
	print(harmming)