#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
def help_info():
	info='''
Usage:
	python3 IndexBaseDistributionCal.py <index.txt> 
Example:
	python3 IndexBaseDistributionCal.py candi_index.txt > result.xls
	
	================candi_index.txt===============
		1	TAGGTCCGAT
		2	GGACGGAATC
		3	CTTACTGCCG
		4	ACCTAATTGA
		...
	===============================================
	
	=================result format=================
	#Base	1	2	3	4	5	6	7	8	9	10
	A	10	10	10	10	10	10	10	10	10	10
	C	10	10	10	10	10	10	10	10	10	10
	G	10	10	10	10	10	10	10	10	10	10
	T	10	10	10	10	10	10	10	10	10	10
	================================================
	'''
	print(info.rstrip())
	exit(0)

def seq2list(file):
	col={}
	A_num=[]
	C_num=[]
	G_num=[]
	T_num=[]
	with open(file,'r') as fh:
		baseA,baseC,baseG,baseT=['','','','']
		for line in fh:
			lines=line.split()
			seqs=list(lines[1].upper().strip())
			seq_len=len(seqs)
			for i in range(len(seqs)):
				col.setdefault(i,[]).append(seqs[i])
		for site in col.keys():
			A_num.append(col[site].count('A'))
			C_num.append(col[site].count('C'))
			G_num.append(col[site].count('G'))
			T_num.append(col[site].count('T'))
		baseA='A'+'\t'+'\t'.join(str(i) for i in A_num)
		baseC='C'+'\t'+'\t'.join(str(i) for i in C_num)
		baseG='G'+'\t'+'\t'.join(str(i) for i in G_num)
		baseT='T'+'\t'+'\t'.join(str(i) for i in T_num)
		return baseA,baseC,baseG,baseT,seq_len
def main():
	if len(sys.argv) !=2:
		help_info()
		
	baseA,baseC,baseG,baseT,seq_len=seq2list(sys.argv[1])
	print('#Base',end='\t')
	for i in range(seq_len):
		print(i+1,end='\t')
	print()
	print(baseA,baseC,baseG,baseT,sep="\n")

if __name__=='__main__':
	main()