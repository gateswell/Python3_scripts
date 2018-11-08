#!/usr/bin/python
import sys

trans ={
	'A':'T',
	'G':'C',
	'C':'G',
	'T':'A',
}
revere = []
#reverse seqence
def reverse_seq(seq):
	rseq =[]
	for i in range(len(seq),0,-1):
		rseq.append(trans[seq[i-1]])
	new_seq = ''.join(rseq)
	return new_seq

with open(sys.argv[1],'r') as fh:
	for line in fh:
		if line.startswith('>'):
			continue
		seq =line.rstrip()
		#Traversal all possible seqence 
		for i in range(len(seq)):
			for j in range(len(seq),i,-1):
				if j-i >=4 and j-i <=12:	#strict size between 4 and 12
					if reverse_seq(seq[i:j]) == seq[i:j]:
						length = j-i
						print(str(i+1)+' '+str(length))