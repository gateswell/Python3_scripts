#!/usr/bin/python
import sys
seq =[]
hash ={}
def readfasta(file):
	with open(file,'r')as fh:
		for line in fh:
			if line.startswith('>'):
				pass
			else:
				line.rstrip()
				seq.append(line)
		return seq
def fragment(seq_list):
	fra = []
	for i in range(len(seq_list[0])):
		for j in range(len(seq_list[0]),i,-1):
			fra.append(seq_list[0][i:j])
	return fra
			
def main(infile):
	seq_list = readfasta(infile)
	frags = fragment(seq_list)
	for i in range(len(frags)):
		result =[]
		for j in seq_list:
			r= j.count(frags[i])
			if r != 0:
				result.append(r)
		if len(result) >= len(seq_list):
			print(frags[i])
			break
			
main(sys.argv[1])