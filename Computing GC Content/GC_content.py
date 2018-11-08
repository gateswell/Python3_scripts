#!/usr/bin/python
import sys
from operator import itemgetter

hash ={}
GC_hash={}
values=[]
with open(sys.argv[1],'r') as fh:
	for line in fh:
		line = line.rstrip()
		if line.startswith('>'):
			name = line.strip('> ')
			hash[name] =''
		else:
			hash[name] += line
for key,value in hash.items():
	num = len(value)
	GC = value.count('G')+value.count('C')
	GCcontent = float(GC/num)*100
	GC_hash[key] = GCcontent
	values.append(GC_hash[key])
sortedGCContent = sorted(GC_hash.items(), key = itemgetter(1))	#hash转换为二维数组 sortedGCContent = [('Rosalind_5959', 0.5357142857142857), ('Rosalind_6404', 0.5375), ('Rosalind_0808', 0.6091954022988506)]
largeName = sortedGCContent[-1][0]
largerGCcontent = sortedGCContent[-1][-1]
print("%s\n%.6f"%(largeName,largerGCcontent))