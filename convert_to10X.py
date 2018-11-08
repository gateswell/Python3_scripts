#!/usr/bin/python
import sys
import gzip

if sys.argv[1] endswith('gz'):
	fh = gzip.open(sys.argv[1],'r')
else:
	fh = open(sys.argv[1],'r')
	
if sys.argv[2] endswith('gz'):
	fh2 = gzip.open(sys.argv[2],'r')
else:
	fh2 = open(sys.argv[2],'r')
	
out_fq1 = gzip.open('fq1.fq.gz','w')
out_fq2 = gzip.open('fq2.fq.gz','w')

while True:
	head1 = fh.readline()
	if not head1:
		break
	seq1  = fh.readline()
	plus1 = fh.readline()
	qual1 = fh.readline()
	head2 = fh2.readline()
	seq2  = fh2.readline()
	plus2 = fh2.readline()
	qual2 = fh2.readline()
	
	fq2_insert  = seq2[:100]
	fq2_index   = seq2[-8:]
	
	fq2q_insert  = qual2[:100]
	fq2q_index   = qual2[-8:]
	
	fq1_new_seq  = fq2_index.strip('\n')
	fq1_new_qual = fq2q_index.strip('\n')
	
	fq2_new_seq = seq1.strip('\n')
	fq2_new_qual = qual1.strip('\n')
	fq2_new_seq2 = fq2_insert.strip('\n')
	fq2_new_qual2= fq2q_insert.strip('\n')
	
	out_fq1.write(head1+fq1_new_seq+'\n'+plus1+fq1_new_qual+'\n')
	out_fq2.write(head2+fq2_new_seq+'\n'+plus2+fq2_new_qual+'\n'+head2+fq2_new_seq2+'\n'+plus2+fq2_new_qual2+'\n')
		
out_fq1.close()
out_fq2.close()