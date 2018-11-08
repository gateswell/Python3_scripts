#!/usr/bin/env python
from random import randint as rd

def random_base(seq_len):
	random_seq = ''
	for i in range(seq_len):
		base = 'ATGC'[rd(0,3)]
		random_seq += base
	return random_seq

def generate_lanes(lanes_num,length1,length2):
	total =''
	try :
		length1 != 0 or length2 != 0 and length1 <= length2
	except ValueError:
		print("length1 and length2 can't be 0")
	for i in range(lanes_num):
		seq = random_base(rd(length1,length2))
		total += seq + '\n'
	return total.strip('\n')

print(generate_lanes(10,100,200))