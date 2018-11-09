#!/usr/bin/python
import sys

def trans_protein(seq):	#trans DNA to protein
	pro=[]
	protein =''
	codon={
	'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
	'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
	'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
	'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
	'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
	'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
	'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
	'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W',
	}
	for i in range(0,len(seq)-3,3):
		pro.append(codon[seq[i:i+3]])
	protein = ''.join(pro)
	return protein
#print(trans_protein('ATGGTCTACATAGCTGACAAACAG'))

def seq_gather(file):	# collect gene sequence and its introns
	sequence =[]
	with open(file,'r') as fh:
		for line in fh:
			if not line.startswith('>'):
				sequence.append(line.rstrip())
		return sequence
		
def main(file):	#delete intron
	seq_list = seq_gather(file)
	for i in range(len(seq_list)):
		if seq_list[i+1] in seq_list[0]:
			seq_list[0] = seq_list[0].replace(seq_list[i+1],'')
		return trans_protein(seq_list[0])

print(main(sys.argv[1]))