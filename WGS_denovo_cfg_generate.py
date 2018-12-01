#!/usr/bin/python
#!encoding:utf8
import sys
import re
import os

usage='''
python3 WGS_denovo_assemble_cfg_generate.py <fqdir> <read length>
'''
if len(sys.argv) <=1:
	print(usage)
	sys.exit(0)

def fqdir_read(fqdir):
	fqlist=[]
	prefhash={}
	fullpath={}
	fq1_full={}
	fq2_full={}
	fqlist=os.listdir(fqdir)
	for fq in fqlist:
		if re.search('1.fq.gz',fq):
			fq_name=re.search('(.*)_1.fq.gz',fq)
			fq_prefix=fq_name.group(1)
			prefhash[fq_prefix]=1
			fullpath[fq_prefix]=os.path.abspath(fqdir)
			fq1_full[fq_prefix]=os.path.abspath(fqdir)+'/'+fq_prefix+'_1.fq.gz'
			fq2_full[fq_prefix]=os.path.abspath(fqdir)+'/'+fq_prefix+'_2.fq.gz'
	for key,value in prefhash.items():
		#return(key+'\t'+fq2_full[key])
		print(cfg_generate(key,fq1_full,fq2_full))
		
def cfg_generate(fq_prefix,fq1_full,fq2_full):
	'''return('[LIB]')
		return('name='+fq_prefix)
		return('avg_ins=300') #insert size needed to be modified in the future
		return('reverse_seq=0')
		return('asm_flags=3')
		return('rank=1')
		return('pair_num_cutoff=3')
		return('map_len=32')
		return('q1='+fq1_full[fq_prefix])
		return('q2='+fq2_full[fq_prefix]+'\n')
		'''
	content='[LIB]\nname='+fq_prefix+'\navg_ins=300\nreverse_seq=0\nasm_flags=3\nrank=1\npair_num_cutoff=3\nmap_len=32\nq1='+fq1_full[fq_prefix]+'\nq2='+fq2_full[fq_prefix]+'\n'
	return(content)
def main():
	print('max_rd_len='+sys.argv[2]+'\n')
	fqdir_read(sys.argv[1])

if __name__ == '__main__':
	main()
