#!/usr/bin/env/python3

string = "ACGTGGGGAGTTGAGTGTCGATACGAACTAGGTAAGGCCAGTAAGGTGCGCCATGCACCCTTACGCGGCTTGCAAACTAACGTGATTACGACTGGGCCCTGTGTCGGTATAGAATAGATTAGATTATAGGCAGCTCGGATCTGGGTTCACACTTTCCCGTCTCCGTGCTGCGTTTTAAACTAAGCGGTGTATACTCGGAGCGATTACACCTGTATTTTAAGCGGCTGGGTACATTCGCTATTGTATAGCGTTCTAGATGGATCCGTTGAAAGGCCTCGCAGCAACTTTCCGAAGGTGAGGTGGGGAGCTGAGGATTCCCAATGCCGTTCAATGCGATACATCTAGTAAATCCTTTGCGCTGAGACCGTGCAGGTTCAAACCGTGCAGAGTGGGATTTCCGTCTAGACTGAGGTAGGCGATTTACTTATCTCACCAGGGGCGAACATGTTGCTGTTGCAGTGGCCCTTTGCGACTTGTGCCGGTCCCAATGGGCATGTTAGGAGGGAAGGGGATAAAAAACTCATATTGAGGAAAAGAGGGACCCCGCTTTCGTACGAAGTCGTTCAACCCTCTGCCATGCTAAATTTCTCCTATGAAGTTCATCGTCCCGCAGTTACGCAATCTGTAGGTCCGTTTTCCCGTTGTCTGAGGAATTTACTCCAGTGCGGCTTGCGAAGCGTCGAGCGTTACCGCTTGCGACTACTGTCCTATTTTCGGATCTTGAGGTTTTTTGGGCACAACGTCTATTGGTTCGGTTCCTTTAGGACAAAAGATCGGGTATCTCTACGCAACCACCCTGAAATTTCAATTTACGATGGTCTTCTGGGTCGTGTAACTTGGCTGGACGTCTAGGGGGGTAGCCTCTAAGCGTAATTTAGAGTCCTGATCCCTCCATTTAGAGTTGCGACTCTCGATGACCGAGTTTTGTATGAACGGGTTACGAGGGCTAACTGCCGTGCTCTTAATGCATTTTT"

num_A = string.count('A')
num_T = string.count('T')
num_C = string.count('C')
num_G = string.count('G')

print(num_A)
print(num_C)
print(num_G)
print(num_T)
