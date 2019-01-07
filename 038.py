#Runtime ~0.7s.

import math
import numpy as np

def number_to_list(n):
    n = str(n)
    return list(map(int, n))

def pandigital_check(n):
    n_list = number_to_list(n)
    if 0 in n_list: return False
    if len(n_list) == len(np.unique(n_list)): return True
    else: return False

def arithmetic_sum(n):
    return int((1/2)*n*(n+1))

pandigital_max = 918273645

N=9
for n in range(3, 2+N):
    multipliers = list(range(1, n))

    largest_multiplicand = math.ceil(987654321/arithmetic_sum(n-1))     #Upper bound since 987654321 is the largest possible pandigital number and (1 + 2 + ... + n)m = (1/2)n(n+1)m.
    for multiplicand in range(1, largest_multiplicand):
        products = [multiplicand * multiplier for multiplier in multipliers]
        pandigital_cand = int("".join(str(product) for product in products))

        if len(str(pandigital_cand)) > 9: break     #Numbers are generated in ascending order, so break once past the largest pandigital number.
        if pandigital_cand > pandigital_max and pandigital_check(pandigital_cand):
            pandigital_max = pandigital_cand

print(pandigital_max)
