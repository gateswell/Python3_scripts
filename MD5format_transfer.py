#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys,re,os

def info():
	help_info='''
transfer MD5 file to linux md5sum format
python MD5format_transfer.py <MD5> [outdir]
	'''
	print(help_info)
	sys.exit(0)

def read_file(file):
	try:
		with open(file,'r',encoding='gbk') as fh:
			while fh.readline():
				print(fh.readline())
				fq=fh.readline()
				md5=fh.readline()
				if fh.readline() == '\n':
					pass
				fqname,fqfile=fq.strip().split('：')
				MD5,md5code  =md5.strip().split('：')
				fqname=os.path.basename(fq)
				print(md5,fqname,sep=' ')
	except IOError as e:
		raise e
		
def main():
	if len(sys.argv) <=1:
		info()
	else:
		read_file(sys.argv[1])
	
if __name__ == '__main__':
	main()