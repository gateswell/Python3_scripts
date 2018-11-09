#!/usr/bin/python
import sys
import re
def trans_protein(seq):	#trans DNA to protein
	pro=[]
	pros =[]
	protein =''
	index ={}
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
	sites = [m.start() for m in re.finditer('ATG', seq)]
	for i in sites:
		start_site = i
		while True:
			if codon[seq[i:i+3]] == '':
				break
			pro.append(codon[seq[i:i+3]])
			i += 3
			if i > len(seq)-3 :
				break
		protein = ''.join(pro)
		pros.append(protein)
		index[start_site] = protein
	return index

def find_first_index(index_hash,protein_seq):
	for keys,value in index_hash.items():
		if protein_seq == value:
			return keys

with open(sys.argv[1],'r') as fh:
	seq = fh.readline().strip('\n')
	pro = fh.readline().strip('\n')
	hash = trans_protein(seq)
	site = find_first_index(hash,pro)
	print(site+1)