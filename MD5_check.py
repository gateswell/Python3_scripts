#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
if len(sys.argv) != 3:
	print("python MD5_check.py <windows MD5.txt> <linux MD5.txt>")
	sys.exit(0)
wmd5 = sys.argv[1]
lmd5 = sys.argv[2]

wm = open(wmd5,'r')
lm = open(lmd5,'r')

md5_hash={}
mark = '1'
while mark:
	a=wm.readline()
	b=wm.readline()
	if not b:
		break
	c=wm.readline()
	d=wm.readline()
	e=wm.readline()
	b=b.rstrip()
	name= re.search(r'(\w+).fq.gz',b)
	prefix = name.group(1)
	md5_hash[prefix] = d.rstrip()
	
while mark:	
	A=lm.readline()
	if not A:
		break
	md5,sample=A.split()
	name=re.search(r'(\w+).fq.gz',sample)
	prefix = name.group(1)
	if prefix in md5_hash:
		print(sample+'\t'+'md5 checked!')