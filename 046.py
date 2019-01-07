#Runtime ~0.14s.

import math

def prime_check(cand):
    if cand == 0: return False
    if cand == 1: return False
    for n in range(2, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

#Generate all prime numbers below n.
def prime_list(n):
    primes = [2, 3]
    if n == 1: return []
    if n == 2: return primes[0]
    if n == 3: return primes
    cand = 1
    #Prime numbers greater than 3 lie on either 6k - 1 or 6k + 1 for integer k.
    while 6*cand - 1 <= n:
        x = 6*cand - 1
        y = 6*cand + 1
        if prime_check(x):
            primes.append(x)
        if prime_check(y) and 6*cand + 1 <= n:
            primes.append(y)
        cand += 1
    return primes

def perfect_square_check(cand):
    sqrt = math.sqrt(cand)
    if math.ceil(sqrt) == math.floor(sqrt): return True
    else: return False

def other_conjecture_check(cand, primes):
    for prime in primes:
        square = (cand - prime)/2
        if perfect_square_check(square): return True
    return False

primes = prime_list(33)
cand = 35
while True:
    if prime_check(cand):
        primes.append(cand)
        cand += 2
    elif other_conjecture_check(cand, primes) is False:
        print(cand)
        break
    else: cand += 2
