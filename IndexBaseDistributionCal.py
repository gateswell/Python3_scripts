#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
def help_info():
	info='''
Usage:
	python3 IndexBaseDistributionCal.py <index.txt> 
Example:
	python3 IndexBaseDistributionCal.py candi_index.txt > result.xls
	
	================candi_index.txt==============
	1	TAGGTCCGAT
	2	GGACGGAATC
	3	CTTACTGCCG
	4	ACCTAATTGA
	...
	==============================================
	
	=================result format================
	#Base	1	2	3	4	5	6	7	8	9	10
	A	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25
	C	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25
	G	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25
	T	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25	0.25
	==============================================
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
		line_num=0;
		for line in fh:
			if line.startswith('#'):
				continue
			line_num+=1
			lines=line.split()
			seqs=list(lines[1].upper().strip())
			seq_len=len(seqs)
			for i in range(len(seqs)):
				col.setdefault(i,[]).append(seqs[i])
		for site in col.keys():
			A_num.append("%.2f" %((col[site].count('A'))/line_num))
			C_num.append("%.2f" %((col[site].count('C'))/line_num))
			G_num.append("%.2f" %((col[site].count('G'))/line_num))
			T_num.append("%.2f" %((col[site].count('T'))/line_num))
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