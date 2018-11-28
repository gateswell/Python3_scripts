#!/usr/bin/python
#!encoding:utf8
import sys
import re
import gzip

help='''
	python3 mutation_type_cal.py <vcf.gz>
	'''
base=['A','T','C','G']
num={}
for i in base:
	for j in base:
		if i == j:
			pass
		else:
			types=i+'>'+j
			num[types]=0

with gzip.open(sys.argv[1],'rb') as fh:
	for line in fh:
		line=line.decode().rstrip()
		if line.startswith('#'):
			pass
		else:
			lines=line.split('\t')
			ref,mut=lines[3:5]
			mut_type=ref+'>'+mut
			for key,value in num.items():
				if mut_type in key:
					num[mut_type]+=1

for key,value in num.items():
	print(key,value,sep='\t')
