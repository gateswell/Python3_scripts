#!/usr/bin/python
import sys

def help_info():
	info='''
python issue2.py <bed>
	'''
	print(info.rstrip())
	sys.exit(0)

def get_maxcitation_site(bed):
	try:
		hash={}
		with open(bed,'r') as fh:
			for line in fh:
				if line.startswith('#'):
					break
				[Chr,start,end]=line.strip().split()[0:3]
				for i in range(int(start),int(end)):
					site=Chr+'\t'+str(i)
					if site in hash:
						hash[site]+=1
					else:
						hash[site]=1
		max_citation=max(hash,key=hash.get)
		print(max_citation)
	except EOFError as e:
		print(file," unexist!",sep="\t")

def main():
	if len(sys.argv) != 2:
		help_info()
	get_maxcitation_site(sys.argv[1])

if __name__=='__main__':
	main()