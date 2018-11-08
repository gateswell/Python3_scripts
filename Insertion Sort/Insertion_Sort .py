#!/usr/bin/env python

def insertion_sort(arr):
	for i in range(1,len(arr)):
		start = arr[i]
		j = i-1
		while j>0 and arr[j] > start:
			arr[j],arr[j+1] = arr[j+1],arr[j]
			j -=1
		arr[j+1] = start
	return arr
print(insertion_sort([4,5,6,1,3]))