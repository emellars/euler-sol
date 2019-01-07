#Runtime ~ 9.5s.

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

n_max, m_max = 1000, 1000
pent_pair = []

while len(pent_pair) == 0:
    pent_pair = [[m, n] for n in range(1, n_max) for m in range(1, m_max) if m >= n and pent_add(n, m) and pent_sub(n, m)]
    n_max += 500
    m_max += 500

print(pent(pent_pair[0][0]) - pent(pent_pair[0][1]))
