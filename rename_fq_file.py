#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys,re,os
import csv
#from shutil import copyfile 

def info():
	help_info='''
=================================help info=====================================
Usage:
	python rename_fq_file.py <sampleID barcode relationship file> <fastq file path>
Example:
	python rename_fq_file.py 转化.csv D:\fq地址
Notice:
	please DO NOT provided xlsx or xls format file! you can transfer xlsx format to csv or txt by Excel.
	the header of file must be set as follow, other column names can be added after this two:
	=======format======
	sampleID	barcode		<- header
	smp_ctl1	1		<- content
	smp_tum1	2		...
	===================
Version:
	V1.0
===============================================================================
'''
	print(help_info.rstrip())
	sys.exit(0)

def parse_relationship_file(file):
	name_hash={}
	if file.endswith('.csv'):	#csv格式
		with open(file,'r') as fh:
			fh_csv = csv.DictReader(fh)
			for line in fh_csv:
				if re.match('^\s$',line['sampleID']):	#排除第一列为空的行
					continue
				name_hash[line['barcode']]=line['sampleID']
	elif file.endswith('.txt'):	#txt格式
		with open(file,'r') as fh:
			header=fh.readline()
			for line in fh:
				lines=line.split().rstrip()
				if re.match('^\s$',line[0]):
					continue
				name_hash[lines[1]]=lines[0]
	return name_hash

def parse_fq_path(path,name_hash):
	rename_hash={}
	for root,dirs,files in os.walk(path):
		for fq in files:
			if re.match('(.*)\_(\w+)\_2.fq.gz',fq):	#PE read2
				origin_full_name=os.path.join(root,fq)
				name=re.match('(.*)\_(\w+)\_2.fq.gz',fq)
				barcode=name.group(2)
				if barcode in name_hash:
					new_name=fq.replace(barcode,name_hash[barcode])
					new_full_name=os.path.join(root,new_name)	#改名后的完整路径名
					rename_hash[origin_full_name] = new_full_name
				else:
					sys.stdout.write(origin_full_name+' can\'t be renamed!\n')
			elif re.match('(.*)\_(\w+)\_1.fq.gz',fq):	#PE read1
				origin_full_name=os.path.join(root,fq)
				name=re.match('(.*)\_(\w+)\_1.fq.gz',fq)
				barcode=name.group(2)
				if barcode in name_hash:
					new_name=fq.replace(barcode,name_hash[barcode])
					new_full_name=os.path.join(root,new_name)
					rename_hash[origin_full_name] = new_full_name
				else:
					sys.stdout.write(origin_full_name+' can\'t be renamed!\n')
			elif re.match('(.*)\_(\w+).fq.gz',fq):	#SE
				rigin_full_name=os.path.join(root,fq)
				name=re.match('(.*)\_(\w+).fq.gz',fq)
				barcode=name.group(2)
				if barcode in name_hash:
					new_name=fq.replace(barcode,name_hash[barcode])
					new_full_name=os.path.join(root,new_name)
					rename_hash[origin_full_name] = new_full_name
				else:
					sys.stdout.write(origin_full_name+' can\'t be renamed!\n')
		return rename_hash

def rename_step(rename_hash):
	for origin_name in rename_hash:
		sys.stdout.write('renaming '+origin_name+' to '+rename_hash[origin_name]+'\n')
		os.rename(origin_name,rename_hash[origin_name])
	sys.stdout.write('All done!\n')

def main():
	name_hash={}
	rename_hash={}
	if len(sys.argv) != 3:
		info()
	name_hash=parse_relationship_file(sys.argv[1])
	rename_hash=parse_fq_path(sys.argv[2],name_hash)
	sys.stdout.write('Origin name\t->\tNew name\n')
	for origin_name in rename_hash:
		sys.stdout.write(origin_name+' -> '+rename_hash[origin_name]+'\n')
	mark=input('Do you make sure all above rename candidates are right [Y/N]: ')
	if mark.upper() == 'Y':
		rename_step(rename_hash)
	else:
		sys.exit(0)
		
if __name__=='__main__':
	main()