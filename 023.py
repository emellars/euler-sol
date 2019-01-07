#Runtime ~5.5s.

import math
import numpy as np

#For a list of objects generate all unique pairings and sum each pair individually, returning a list of unique combinations of (m, n) with a value below "limit".
def pairs(array, limit = math.inf):
    return np.unique([sum([m, n]) for m in array for n in array if m <= n and m + n <= limit])

#Returns divisors of a number n by checking factors between 1 and sqrt(n).
def divisors(n):
    divisors_list = []
    ceil_sqrt = math.ceil(math.sqrt(n))
    for k in range(1, ceil_sqrt):
        if n % k == 0:
            divisors_list.append(k)
            if k != 1: divisors_list.append(int(n/k))
    if ceil_sqrt == math.sqrt(n): divisors_list.append(ceil_sqrt)
    return divisors_list

#Returns list of abundant numbers.
def abundants(n):
    return [x for x in range(n) if sum(divisors(x)) > x]

lower_bound = 28123 + 1

abundant_sums = set(pairs(abundants(lower_bound), lower_bound))
integers = set(range(1, lower_bound))
non_abundant_sums = integers.difference(abundant_sums)

print(sum(non_abundant_sums))
