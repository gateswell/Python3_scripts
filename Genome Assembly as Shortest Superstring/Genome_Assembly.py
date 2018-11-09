#!/usr/bin/env python
import sys

def gather_seq(file):	#gather all sequence
	sequence =[]
	with open(file,'r') as fh:
		for line in fh:
			if not line.startswith('>'):
				if line != '':
					sequence.append(line.rstrip())
			else:
				sequence = sequence + line.strip('\n')
		return sequence

def merge_seq(seq_list):
	for num in range(len(seq_list)):
		for i in range(len(seq_list[num])):
			#if seq_list[num][i:] == seq_list[num+1][0:i]:
				#return seq_list[num][0:i]+seq_list[num+1][i:]
			if seq_list[num][i:] in seq_list[num+1]:
				

def main(file):
	file = sys.argv[1]
	sequence = gather_seq(file)
	merge_seq = merge_seq(sequence)
	print(merge_seq)