#Runtime ~0.2s.

import numpy as np

def decimal_palindrome(n):
    part1 = str(n)
    part2 = part1[::-1]
    return [int(part1 + part2), int(part1 + part2[1:])]

def binary_palindrome(n):
    b = bin(n)
    part1 = str(b)
    part2 = part1[::-1][:-2]
    return [part1 + part2, part1 + part2[1:]]

decimal_palindromes = []
binary_palindromes = []
max_number = 1000

#Generate all decimal palindromes up to max_number^2.
for n in range (1, max_number):
    decimal_palindromes.append(decimal_palindrome(n))

#1000000 has 20 digits in binary. Therefore we only need to form binary palindromes no further than  2^10 - 1 (i.e. 1111111111 in binary).
for n in range (1, 2**10 - 1):
    binary_palindromes.append(binary_palindrome(n))

decimal_palindromes = {palindrome for sublist in decimal_palindromes for palindrome in sublist}
binary_palindromes= {palindrome for sublist in binary_palindromes for palindrome in sublist}

binary_palindromes_in_decimal = {int(b, 2) for b in binary_palindromes}

double_palindromes = decimal_palindromes.intersection(binary_palindromes_in_decimal)
print(sum(double_palindromes))
