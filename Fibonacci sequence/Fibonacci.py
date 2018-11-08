#!/usr/bin/python
import os
import sys

def fibo(n,k):
	if n ==1 or n ==2:
		fibo(n,k) = k
	elif n <= 40:
		fibo(n,k) = fibo(n-1,k) + fibo(n-2,k)
	else:
		break
	return fibo(n,k)

n = sys.argv[1]
k = sys.argv[2]
fibo(n,k)