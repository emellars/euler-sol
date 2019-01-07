#Runtime ~ 16s.

import itertools as iter

def string_list_to_string(l):
    return "".join(elem for elem in l)

initial_pandigital = "1234567890"

pandigitals = list(map(string_list_to_string, iter.permutations(initial_pandigital, 10)))
primes = [2, 3, 5, 7, 11, 13, 17]

substring_divisible_pandigitals = []

for pandigital in pandigitals:
    substring_divisibility_count = 0
    for n in range(7):
        if int(pandigital[n+1] + pandigital[n+2] + pandigital[n+3]) % primes[n] == 0: substring_divisibility_count += 1
    if substring_divisibility_count == 7: substring_divisible_pandigitals.append(int(pandigital))

print(sum(substring_divisible_pandigitals))
