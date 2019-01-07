#Runtime ~24s.

import numpy as np

#Check primality of a number.
def prime_check(cand):
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

#Generate list of exponents of prime factors.
def prime_factors(n):
    if prime_check(n): return [2]

    prime_powers = []
    for prime in prime_list(int(n/2+1)):
        count = 1
        factor_candidate = n
        while True:
            if factor_candidate % prime == 0:
                count += 1
                factor_candidate = factor_candidate / prime
            else:
                if count > 1: prime_powers.append(count)
                break
    prime_powers = np.array(prime_powers)
    return prime_powers

#Formula for summation of an arithmetic series over {1, 2, 3, ...}.
def triangle_number(n):
    return int((1/2)*n*(n + 1))

divisors = 500
count = 0
n = 1

#n and n+1 have unique prime factors. Using the triangle_number formula, the number of factors can therefore be determined from the prime factors of n and n+1.
while count < divisors:
    n += 1
    if n % 2 == 0:
        x = prime_factors(n/2)
        y = prime_factors(n+1)
    else:
        x = prime_factors(n)
        y = prime_factors((n+1)/2)
    triangle_factors = np.concatenate((x, y))
    count = np.prod(triangle_factors)

print(triangle_number(n))
print(count)
