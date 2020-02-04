#!/usr/bin/env/python

import re 

def get_gc_content(sequence):
	seq_length = len(sequence)
	g_content = sequence.count("G")
	c_content = sequence.count("C")
	gc_content = ((g_content + c_content)/seq_length)*100
	return gc_content 
	
fasta = open("/Users/haydenthomas/Desktop/use_rosalind_gc.txt")

names = None 
seqs = dict()
for line in fasta: 
	#discard the newline at the end 
	line = line.rstrip()
	#distinguish header from sequence 
	if line.startswith('>'): 
		names = line[1:] #this discards the '>' but keeps the id 
		seqs[names] = ''
	else: 
		seqs[names] = seqs[names]+line

slist = list()

for i in seqs.values():
	slist.append(i)


print(seqs.keys())
for m in slist: 
	print(get_gc_content(m))