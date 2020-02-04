#!/usr/bin/env/python

import itertools 

a = '12345'
perm = itertools.permutations(a)

for i in perm: 
	print(i)


# Text processing

###Haydens-MacBook-Pro:desktop haydenthomas$ python enumerating_gene_orders.py > a.txt
###Haydens-MacBook-Pro:desktop haydenthomas$ tr -d "()" < a.txt > b.txt
###Haydens-MacBook-Pro:desktop haydenthomas$ tr -d "," < b.txt > c.txt
###Haydens-MacBook-Pro:desktop haydenthomas$ tr -d "'" < c.txt > d.txt
###Haydens-MacBook-Pro:desktop haydenthomas$ open d.txt###