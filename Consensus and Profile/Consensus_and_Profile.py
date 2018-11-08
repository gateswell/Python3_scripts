#!/usr/bin/python
import sys
with open(sys.argv[1],'r') as fh:
	fa =[]
	A,C,G,T = [],[],[],[]
	counter = {'A':[],'T':[],'C':[],'G':[]}
	consensusSeq =''
	for line in fh:
		if line.startswith('>'):
			continue
		else:
			line=line.rstrip()
			fa.append(line)
	
	'''for base in counter:
		base_total =[]
		for i in range(len(fa)):
			column = [x[i] for x in fa]
			number = column.count(base)
			#counter[base].append(number)
			base_total.append(number)

		print('%s: %s' % (base,base_total), end = '\n')
	i	'''
	index =[]
	for i in range(len(fa)):
		column = [x[i] for x in fa]
		A.append(column.count('A'))
		T.append(column.count('T'))
		G.append(column.count('G'))
		C.append(column.count('C'))