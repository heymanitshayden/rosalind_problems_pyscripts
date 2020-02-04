#!/usr/env/bin/python

###Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive. 
###Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.###

def mendel_first_law(x,y,z): 
	
	k = x
	m = y
	n = z
	
	population_sum = k + m + n 
	
	probability_equation = (4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1))/(4*population_sum*(population_sum-1))
	
	return probability_equation 
	
print('The probability of a dominant phenotype is: ' + str(mendel_first_law(19,15,18)))
