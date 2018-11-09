#!/usr/bin/python
import sys

with open(sys.argv[1],'r') as fh:
	hash = {}
	for line in fh:
		lines = line.split()
		for i in range(len(lines)):
			if i%2 ==0:
				hash[lines[i]] = lines[i+1]
seq = input("pls dial RNA sequence:")
if len(seq)%3 != 0:
	print("RNA base number incorrect")
else:
	protein_seq =''
	for i in range(0,len(seq),3):
		if hash[seq[i:i+3]] == 'Stop':
			continue
		else:
			protein_seq += hash[seq[i:i+3]]
	print(protein_seq)