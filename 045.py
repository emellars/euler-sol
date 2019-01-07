#Runtime ~0.1s.

import math

def tri(t):
    return int(t*(t + 1)/2)

#t and p are the indices for triangular and pentagonal numbers. Equating some triangular number with some pentagonal number yields the relation t(t + 1) = p(3p - 1), from which an equation for p may be derived for a given t. Therefore, one can check if a triangular number is pentagonal by requiring that the aforementioned equation be an integer for integer t.
def tri_pent_check(t):
    p = (1/6)*(math.sqrt(12*t**2 + 12*t + 1) + 1)
    if math.ceil(p) == math.floor(p): return True
    else: return False

#Note that, by similarly comparing triangular and hexagonal numbers, t(t+1) = 2h(2h-1). This has solutions t = -2h and t = 2h - 1, the latter of which is relevant. Hence, every triangle number with odd index is also a hexagonal number.

t=287
while True:
    if tri_pent_check(t): break
    t += 2

print(tri(t))
