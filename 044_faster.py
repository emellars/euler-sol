#Runtime ~3.2s.

import math

def pent(n):
    return int(n*(3*n - 1)/2)

#Equation for k where P_k = P_m + P_n. Returns "True" when k is an integer.
def pent_add(m, n):
    k = (1/6)*(math.sqrt(36*(n**2 + m**2) - 12*(n + m) + 1) + 1)
    if math.ceil(k) == math.floor(k): return True
    else: return False

#Equation for l where P_l = P_m - P_n. Returns "True" when l is an integer.
def pent_sub(m, n):
    l = (1/6)*(math.sqrt(36*(n**2 - m**2) - 12*(n - m) + 1) + 1)
    if math.ceil(l) == math.floor(l): return True
    else: return False

pent_indices = list(range(1, 3))
n = 3

finished = False
while finished == False:
    for elem in pent_indices:
        if pent_add(elem, n) and pent_sub(elem, n):
            print(pent(n) - pent(elem))
            finished = True
    pent_indices.append(n)
    n += 1
