#Runtime ~1.85s.

import math
import numpy as np

def number_to_list(n):
    n = str(n)
    return list(map(int, n))

#Checks if number is composed of unique digits (additionally returning false if the number contains 0).
def unique_digits(n):
    n_list = number_to_list(n)
    if 0 in n_list: return False
    elif len(n_list) == len(np.unique(n_list)): return True
    else: return False

#For a list of objects generate all unique pairings which are potentially pandigital. (Note that any product with five digits requires a multiplican and multiplier which have at least 5 digits, so they won't form a pandigital product.)
def pandigital_cands(array, m_limit = math.inf, n_limit = math.inf):
    return [[m, n] for m in array for n in array if m <= n and m < m_limit and n < n_limit and len(str(m*n)) < 5 and unique_digits(int(str(m) + str(n)))]

#Note that 2*5000 = 10000 which uses 10 digits; this is an upper bound for the multiplier. Note also that 100*100=10000 which has 11 digits; this is an upper bound for the multiplican.
pan_pairs = pandigital_cands(range(1, 5000), 100, 5000)
pan_products = list(map(np.prod, pan_pairs))

#Remove elements from pan_pairs and pan_products if the product contains repeat digits.
for product in pan_products:
    if unique_digits(product) is False:
        d = pan_products.index(product)
        del pan_pairs[d]
        del pan_products[d]

#Create list of pandigital products where the multiplican, multiplier, and product are, together, pandigital.
pan_all = []
for x in range(len(pan_products)):
    all_digits = int(str(pan_pairs[x][0]) + str(pan_pairs[x][1]) + str(pan_products[x]))
    if unique_digits(all_digits) and len(str(all_digits)) == 9:
        pan_all.append(pan_products[x])

print(sum(np.unique(pan_all)))
