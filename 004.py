#Runtime ~0.3s.

import numpy as np

#Generate a palindrome from a number.
def palindrome(n):
    part1 = str(n)
    part2 = part1[::-1]
    return [int(part1 + part2), int(part1 + part2[1:])]

#Generate array containing all multiples formed from multiplying two numbers each with a value no larger than max_number - 1.
multiples = []
max_number = 1000
for n in range(1, max_number):
    for m in range (n, max_number):
            multiples.append(n * m)

#Generate array containg all palindromes with value less than 1000^2.
palindromes=[]
for n in range (1, max_number):
    palindromes.append(palindrome(n))

palindromes = [palindrome for sublist in palindromes for palindrome in sublist] #Flatten the list.

multiples=np.array(multiples)
palindromes=np.array(palindromes)

#Intersection of both arrays gives palindromes that can be factored into two numbers.
factored_palindromes=np.intersect1d(multiples, palindromes)
print(factored_palindromes[-1])
