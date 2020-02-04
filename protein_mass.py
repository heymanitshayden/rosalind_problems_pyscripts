#!/usr/bin/env/python 
from decimal import *
protein_mass = {
'A':71.03711, 'C':103.00919, 'D':115.02694, 'E':129.04259, 'F':147.06841, 
'G':57.02146, 'H':137.05891, 'I':113.08406, 'K':128.09496, 'L':113.08406,
'N':114.04293, 'P':97.05276, 'Q':128.05858, 'R':156.10111, 'M':131.04049,
'S':87.03203, 'T':101.04768, 'V':99.06841, 'W':186.07931, 'Y':163.06333}

file = raw_input("Path to file: ")

f = open(file, 'r')

if f.mode == 'r': 
	seq = f.read()

def get_mass(seq): 
	
	mass = list()
	for aa in seq: 
		aa_mass = protein_mass.get(aa)
		if aa_mass: 
			mass.append(aa_mass)
	mass_sum = Decimal(sum(mass))
	
	return mass_sum
		
print(get_mass(seq))