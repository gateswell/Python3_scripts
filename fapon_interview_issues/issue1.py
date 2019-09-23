#!/usr/bin/python
import sys

def help_info():
	info='''
python issue1.py <seqeunce list>
	'''
	print(info.rstrip())
	sys.exit(0)

def count_seq(file):
	try:
		hash={}
		with open(file,'r') as fh:
			while True:
				seq=fh.readline().strip()
				if not seq:
					break
				if seq in hash:
					hash[seq]+=1
				else:
					hash[seq]=1
		for seq,num in hash.items():
			print(seq,num,sep='\t')
	except EOFError as e:
		print(file," unexist!",sep="\t")

def main():
	if len(sys.argv) != 2:
		help_info()
	count_seq(sys.argv[1])

if __name__=="__main__":
	main()