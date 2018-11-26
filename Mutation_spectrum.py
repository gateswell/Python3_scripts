#!usr/bin/python
#!encoding:utf8
import sys
import re
import gzip

if len(sys.argv) < 1:
	print('python3 Mutation_spectrum.py <vcf.gz>')
	sys.exit(1)
variant={
		'T>C/A>G':0,
		'C>T/G>A':0,
		'C>A/G>T':0,
		'T>A/A>T':0,
		'T>G/A>C':0,
		'C>G/G>C':0
		}
with gzip.open(sys.argv[1],'rb') as fh:
	for line in fh:
		line=line.decode().rstrip()
		if line.startswith('#'):
			pass
		else:
			lines=line.split('\t')
			mut=lines[3]+'>'+lines[4]
			for key,value in variant.items():
				if mut in key:
					variant[key] += 1
for key,value in variant.items():
	print(key+'\t'+str(value))
