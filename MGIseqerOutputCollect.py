#!/usr/bin/python
# -*- coding:utf-8 -*-

import re,os,sys
import time,datetime
from shutil import copyfile

def help_info():
	info='''
============================================================================
Usage:
	python MGIseqerOutputCollect.py <chip name> <date:20190101> <outdir>
Example:
	python MGIseqerOutputCollect.py V300018621 20190101 D:\tmp
Version:
	V1.0.0.0
Note:
	The Script can be run by python2 or python3 
	outdir will be created if outdir unexists, the default outdir is D:\CopyData
	contact with caoshuhuan@yeah.net if any bug happened during runing.
============================================================================
'''
	print(info.rstrip()) 
	exit(0)
	
if len(sys.argv)<3:	#outdir can be dismissed
	help_info()
	
def print_time():
	return time.strftime("[%Y-%m-%d %H:%M:%S] ",time.localtime())

def get_days(date,num=10):	#date format:20190101
	format_date=datetime.datetime(year=int(date[:4]),month=int(date[4:6]),day=int(date[6:]))	#2019-01-01
	#date=int(date)
	alldays=[]
	for i in range(num):
		be4day=format_date-datetime.timedelta(days=i)
		format_be4day=be4day.strftime("%Y%m%d")
		alldays.append(format_be4day)
		#print format_befday
	return alldays

# copy chip png and tif files
def copy_DataThumbFOVFigs(dir,chipname,outdir):
	try :
		for lane in os.listdir(dir):
			if lane != 'Metrics':
				if not os.path.exists(outdir+'\\'+chipname+'\\'+lane):
					os.makedirs(outdir+'\\'+chipname+'\\'+lane)
					
				for files in os.listdir(dir+'\\'+lane+'\\S01'):
					#if files.startswith('Thumbnail'):	#copy thumbnail figures
					if re.search(r'C004R036|Thumbnail',files):
						fullname=dir+'\\'+lane+'\\S01\\'+files
						outputname=outdir+'\\'+chipname+'\\'+lane+'\\'+files
						if not os.path.exists(outputname):
							copyfile(fullname,outputname)
							sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')
					else:
						sys.stdout.write('No such files: '+files+' \n')
						continue
					'''if re.search(r'C004R036',files):	#copy FOV C004R036 figures
						fullname=dir+'\\'+lane+'\\S01\\'+files
						outputname=outdir+'\\'+chipname+'\\'+lane+'\\'+files
						if not os.path.exists(outputname):
							copyfile(fullname,outputname)
							sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')
					else:
						sys.stdout.write('No such files: '+files+' \n')
						continue'''
			else:
				continue
	except IOError as e:
		sys.stdout.write('No such dir: '+dir)
		raise e

def copy_Metrics(dir,chipname,outdir):
	try:
		if not os.path.exists(outdir+'\\'+chipname+'\\Metrics'):
			os.makedirs(outdir+'\\'+chipname+'\\Metrics')
		for Mfile in os.listdir(dir):
			fullname=dir+'\\'+Mfile
			outputname=outdir+'\\'+chipname+'\\Metrics\\'+Mfile
			if not os.path.exists(outputname):
				copyfile(fullname,outputname)
				sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')
	except IOError as e:
		sys.stdout.write('No such dir: '+dir)
		raise e

def copy_ResultStatHtml(dir,chipname,outdir):
	for lane in os.listdir(dir):
		if not os.path.exists(outdir+'\\'+chipname+'\\'+lane):
			os.makedirs(outdir+'\\'+chipname+'\\'+lane)
		for files in os.listdir(dir+'\\'+lane):
			if re.search('BarcodeStat|SequenceStat',files):
				fullname=dir+'\\'+lane+'\\'+files
				outputname=outdir+'\\'+chipname+'\\'+lane+'\\'+files
				if not os.path.exists(outputname):
					copyfile(fullname,outputname)
					sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')
				'''else:
					sys.stdout.write(outputname+'exists.\n')
					continue'''
			if re.search(r'html',files):
				fullname=dir+'\\'+lane+'\\'+files
				outputname=outdir+'\\'+chipname+'\\'+lane+'\\'+files
				if not os.path.exists(outputname):
					copyfile(fullname,outputname)
					sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')
				'''else:
					sys.stdout.write(outputname+'exists.\n')
					continue'''

def copy_BGI_logs(dir,date,chipname,outdir):
	alldays=get_days(date,10)
	if not os.path.exists(outdir+'\\'+chipname+'\\BGI_logs'):
		os.makedirs(outdir+'\\'+chipname+'\\BGI_logs')
	for logs in os.listdir(dir):
		if re.search(r'BGI.Zebra(.*)-(20\d+).',logs):
			logfiles=re.search(r'BGI.Zebra(.*)-(20\d+).',logs)
			outdate=logfiles.group(2)
			if outdate in alldays :	# keep 10 days logs before date
				fullname=dir+'\\'+logs
				outputname=outdir+'\\'+chipname+'\\BGI_logs\\'+logs
				if not os.path.exists(outputname):
					copyfile(fullname,outputname)
					sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')	
			else:
				#sys.stdout.write('file: '+logs+' unsupported\t'+outdate+'\n')
				continue

def copy_processor(dir,date,chipname,outdir):
	alldays=get_days(date,10)
	if not os.path.exists(outdir+'\\'+chipname+'\\processor'):
		os.makedirs(outdir+'\\'+chipname+'\\processor')
	for txt in os.listdir(dir):
		if re.search(r'processor_(20\d+)_(.*).',txt):	#processor_20190707_001625-HR.txt
			logfiles=re.search(r'processor_(20\d+)_(.*).',txt)
			outdate=logfiles.group(1)
			if outdate in alldays  :	# keep 10 days logs before date
				fullname=dir+'\\'+txt
				outputname=outdir+'\\'+chipname+'\\processor\\'+txt
				if not os.path.exists(outputname):
					copyfile(fullname,outputname)
					sys.stdout.write(print_time()+'Copy file: '+fullname+'\n')
		else:
			sys.stdout.write('No Such File or directory: '+txt+'\n')

def main():
	chipname=sys.argv[1].upper()
	dirD="D:\\Data\\"+chipname
	dirM="D:\\Data\\"+chipname+"\\Metrics"
	dirR="D:\\Result\\OutputFq\\"+chipname
	dirL="C:\\BGI\\Logs"
	dirZ='C:\\ZebraCallV2\\V1.0.7.197'
	date=sys.argv[2]
	outdir=''
	if len(sys.argv) ==4:
		outdir=sys.argv[3]
	elif len(sys.argv) ==3:
		outdir='D:\\CopyData'
	copy_DataThumbFOVFigs(dirD,chipname,outdir)
	copy_Metrics(dirM,chipname,outdir)
	copy_ResultStatHtml(dirR,chipname,outdir)
	copy_BGI_logs(dirL,date,chipname,outdir)
	copy_processor(dirZ,date,chipname,outdir)

if __name__ == '__main__':
	main()