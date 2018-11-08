#!/usr/bin/python

string1 = input("pls input long sequence:")
string2 = input("pls input short sequence:")

if len(string1) > len(string2):
	length = len(string2)
	for i in range(len(string1)):
		if string2 == string1[i:i+length]:
			print(i+1)
		else:
			continue
			print('not match')
else:
	print('long sequence must be longer than short one')