#!/usr/bin/python
import sys

def Reverse_base(seq):
	trans ={'A':'T',
		'T':'A',
		'G':'C',
		'C':'G',
		}
	rev_seq=''
	for i in range((len(seq)-1),-1,-1):
		rev_seq += trans[seq[i]]
	return rev_seq

with open(sys.argv[1],'r') as fh:
	for line in fh:
		lines=line.rstrip().split()
		new_line=Reverse_base(lines[-1])
		print(lines[0]+'\t'+Reverse_base(lines[-1]))

