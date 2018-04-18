#!/usr/bin/env python
import sys
import os

trans = {
	'A' : 'T',
	'G' : 'C',
	'T' : 'A',
	'C' : 'G',
}

def complement(s):
	return "".join(trans[i] for i in s)

with open(sys.argv[1]) as fh1:
	for line in fh1:
		print(complement(line))