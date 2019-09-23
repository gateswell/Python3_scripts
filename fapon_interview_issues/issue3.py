#!/usr/bin/python
import sys

def help_info():
	info='''
Useage:
	python issue3.py <brcaket list>
Example:
	python issue3.py ({[]}{})[]
	'''
	print(info.rstrip())
	sys.exit(0)

def determin_properly_close_ornot(sentence):
	try:
		hash={}
		complement={
			'{':'}',
			'[':']',
			'(':')'
		}
		for i in range(len(sentence)):
			bracket=sentence[i]
			if bracket in complement:
				if complement[bracket] in hash:
					hash[complement[bracket]]+=1
				else:
					hash[complement[bracket]]=1
			else:
				if bracket in hash:
					hash[bracket] +=1
				else:
					hash[bracket] =0
		j=0
		for key,value in hash.items():
			if value%2 != 0:
				print(key +' lost partner bracket')
				j+=1
		if j == 0:
			print("All bracket are paired!")
	except IOError as e:
		print("bracket list unexist!")

def main():
	if len(sys.argv) != 2:
		help_info()
	determin_properly_close_ornot(sys.argv[1])

if __name__=='__main__':
	main()