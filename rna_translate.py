#!/usr/bin/env/python

gencode = {
'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}

f = open("/Users/haydenthomas/desktop/rna.txt","r")
if f.mode == "r": 
	rna = f.read()
	
def get_protein(rna): 
	protein = ""
	last_codon_start = len(rna)-2
	for start in range(0,last_codon_start,3):
		codon = rna[start:start+3]
		amino_acid = gencode.get(codon)
		protein = protein + amino_acid 
	return protein 
	

print("protein sequence is: " + get_protein(rna))