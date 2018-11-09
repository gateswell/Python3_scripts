#!/usr/bin/env python
#import sys
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('vcf1', type=str, help='the first vcf file')
parser.add_argument('vcf2', type=str, help='the second vcf file')
args = parser.parse_args()

vcf1 = args.vcf1
vcf2 = args.vcf2

name1=os.path.basename(vcf1).rstrip('.vcf')
name2=os.path.basename(vcf2).rstrip('.vcf')
#print(name1)
total1=[]
total2=[]
v1_s = open(name1+'_specific.vcf','w')
v2_s = open(name2+'_specific.vcf','w')
both = open(name1+'_'+name2+'_both.vcf','w')
with open(vcf1,'r') as v1:
	for line in v1:
		if not line.startswith('#'):
			lines = line.rstrip().split('\t')
			if re.search('SOMATIC|PASS',line) && len(lines[3])==len(lines[4])==1:
				outline = '\t'.join(lines[:4])
				total1.append(outline)
with open(vcf2,'r') as v2:
	for line in v2:
		if not line.startswith('#'):
			lines = line.rstrip().split('\t')
			if re.search('SOMATIC|PASS',line) && len(lines[3])==len(lines[4])==1:
				outline = '\t'.join(lines[:4])
				



'''for key,value in hash1.items():
	if hash1[key] == 1:
		v1_s.write(key,'\n')
	elif hash1[key] == 2:
		v2_s.write(key,'\n')
	elif hash1[key] ==3:
		both.write(key,'\n')'''
v1_s.close()
v2_s.close()
both.close()
