#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,sys,re
import xlwt

def help_info():
	info='''
Usage:
	python3 txt2xls <txt> [xls]
Example:
	python3 txt2xls a.txt
	python3 txt2xls a.txt b.xls
Note:
The script will generate xls with same prefix name of txt when no output xls provided!'''
	print(info.rstrip())
	exit(0)
	
def out_xls(input,output=None):
	if output:
		return output
	else:
		prefix=os.path.basename(input)
		outdir=os.path.dirname(input)
		prefix=prefix.replace('txt','xls')
		return outdir+'/'+prefix
	
def write_xls(file_handle,output):
	row_list=[]
	for line in file_handle:
		row_list.append(line.split('\t'))
	workbook=xlwt.Workbook()
	worksheet=workbook.add_sheet('Sheet1')
	i=0
	for column in row_list:
		for item in range(len(column)):
			worksheet.write(i,item,column[item])
		workbook.save(output)
		i+=1

def main():
	if len(sys.argv) <2:
		help_info()
	with open(sys.argv[1]) as fh:
		if len(sys.argv) ==3 :
			output=out_xls(sys.argv[1],sys.argv[2])
			write_xls(fh,output)
		else:
			output=out_xls(sys.argv[1])
			write_xls(fh,output)

if __name__=="__main__":
	main()