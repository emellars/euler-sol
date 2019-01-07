#Runtime ~0.72s.

import itertools as iter

def prime_check(cand):
    if cand == 0: return False
    if cand == 1: return False
    for n in range(2, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

def string_list_to_num(l):
    return int("".join(elem for elem in l))

pandigital_to_check = "0987654321"

#Start with largest 9-digit pandigital number. Check for primes and descend down. If none found, repeat with 8-digit pandigital numbers. Continue until a prime is found.
finished = False
while finished == False:
    pandigital_to_check = pandigital_to_check[1:]
    pandigitals = list(map(string_list_to_num, iter.permutations(pandigital_to_check, len(pandigital_to_check))))

    for pandigital in pandigitals:
        if prime_check(pandigital):
            print(pandigital)
            finished = True
            break
