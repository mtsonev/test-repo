# A trivial program that can generate a DNA sequence 
import random
def DNA_random_seq(n):
    nucleotide = ['A', 'G', 'T', 'C']
    output = ''
    for i in range(n):
        output += random.choice(nucleotide)
    return str(output)