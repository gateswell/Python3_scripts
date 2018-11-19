#!/usr/bin/python
'''
calculate the overlap size between PE reads'''
import pysam
import sys
import os
import re

def readbam(bam):
	overlap=[]
	readNum=0
	overNum=0
	try:
		samfile=pysam.AlignmentFile(bam,'rb')
	except Exception as e:
		raise e
	for line in samfile:
		if line.startswith('@'):
			continue
		readNum +=1
		lines=line.split('\t')
		cigar=lines[5]
		if re.search('[IDNSHPX=]',cigar):
			continue
		else:
			if lines[6] == '=' and lines[8] <= len(lines[9])*2 and lines[8] > 0:
				size=len(lines[9])-lines[8]
				overlap.append(size)
				overNum+=1
		return overlap,readNum,overNum

def main():
	overlap,readNum,overNum=readbam(sys.argv[1])
	totalSize=0
	for size in overlap:
		totalSize+=size
	mean_overlapSize = totalSize/overNum
	print('average overlap size:\t'+str(mean_overlapSize)+'\noverlap reads num:\t'+str(overNum)+'\ntotal reads num:\t'+str(readNum))

if __name__ == '__main__': 
	main()
