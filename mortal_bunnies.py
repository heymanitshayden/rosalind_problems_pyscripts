#!/usr/bin/env/python
n = 84
m = 16
bunnies = [1,1]
months = 2 
 
while months < n: 
	if months <m: 
		bunnies.append(bunnies[-2] + bunnies[-1])
	
	elif months == m or months == m+1: 
		bunnies.append(bunnies[-2] + bunnies[-1] -1)
	
	else: 
		bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(m + 1)])
	
	months += 1
	
print(bunnies[-1])
