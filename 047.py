#Runtime ~20s.

import math

def prime_check(cand):
    for n in range(2, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

#Generate all prime numbers below n.
def prime_list(n, primes):
    if n <= primes[-1]: return [prime for prime in primes if prime <= n]
    else:
        #Prime numbers greater than 3 lie on either 6k - 1 or 6k + 1 for integer k > 1.
        if (primes[-1] + 1) % 6 == 0:
            cand = int((primes[-1] + 1)/6 + 1)
            if prime_check(primes[-1] + 2): primes.append(primes[-1] + 2)
        else:
            cand = int((primes[-1] - 1)/6 + 1)

        while 6*cand - 1 <= n:
            x = 6*cand - 1
            y = 6*cand + 1
            if prime_check(x):
                primes.append(x)
            if prime_check(y) and 6*cand + 1 <= n:
                primes.append(y)
            cand += 1
    return primes

#Returns the number of unique prime factors for n.
def distinct_prime_factors(n):
    if prime_check(n): return 1
    unique_factors = 0
    for prime in prime_list(math.floor(n/2), primes):
        if n % prime == 0: unique_factors += 1
    return unique_factors

primes = [2, 3]

count = 0
number_of_factors = 4
n = 6
while count != number_of_factors:
    if distinct_prime_factors(n) == number_of_factors: count += 1
    else: count = 0
    n += 1

print(n - number_of_factors)
