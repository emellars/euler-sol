#Runtime ~175s.

import math

#Product of sequences.
def prod(l):
    product = 1
    for num in l:
        product *= num
    return product

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

#Returns the unique prime factors of n.
def distinct_prime_factors(n, hist):
    if prime_check(n): return [n]
    dpf, m = [], n
    #Generate prime factorisation of n.
    for prime in primes:
        if m % prime == 0:
            m = m//prime
            dpf.append(prime)
            #Check for repeated factors.
            while True:
                #Check if the reduced result m has been factorised previously.
                if "{}".format(m) in hist:
                    dpf = list(set(dpf + hist["{}".format(m)])) #If so concatenate the two lists of factors and retain only unique prime factors.
                    hist["{}".format(n)] = dpf  #Update the dictionary for n.
                    return dpf
                elif m % prime == 0:
                    m = m//prime
                    dpf.append(prime)
                else: break
        #If all the prime factors have been generated, update the dictionary and return the unique prime factors.
        if prod(dpf) == n:
            dpf = list(set(dpf))
            hist["{}".format(n)] = dpf
            return dpf

#Euler's totient function.
def totient(n):
    if n == 1: return 1
    if prime_check(n): return n - 1
    tot = n
    for prime in distinct_prime_factors(n, factor_history):
        tot = tot * (1 - 1/prime)
    return int(tot)


primes, factor_history = [2, 3], dict()
max_number = 10**6
prime_list(max_number//2, primes)   #Generate all primes that could be a factor.

odds = [num for num in range(1, max_number, 2)] #Generate all odd numbers up to max_number.
bins = []   #For integers in the range of 1 to max_number, they are grouped together in bins such that each successive element of the bin is the double of the previous element.
halfway = max_number//4

#The first half of odd numbers can be repeatedly doubled to generate numbers <= max_number. The set of numbers generated from this together with the second half of odd numbers spans exactly the numbers [1, 2, ..., max_number].
for num in odds[:halfway]:
    bin = []
    while num <= max_number:
        bin.append(num)
        num = 2*num
    bins.append(bin)

"""
The bins contain numbers like [1, 2, 4, 8, ...], [3, 6, 12, 24, 48], etc. The property totient(2m)=totient(m), where m is odd, is used for the first two entries in each bin and the property totient(2m)=2*totient(m), where m is even, is used for the rest of the entries. (See https://en.wikipedia.org/wiki/Euler%27s_totient_function#Other_formulae.) The corresponding totients are [\phi_0, \phi_0, 2\phi_0, 4\phi_0, ...].

The first two totients contribute 2*\phi_0 together. The rest of the sequence is then [2^1, 2^2, ..., 2^n]*\phi_0 where n is the number of elements in this list. Their contribution is S = (2^1 + 2^2 + ... + 2^n)\phi_0.

Note that 2S = (2^2 + 2^3 + ... + 2^(n+1))\phi_0, so that 2S - S  =   S and therefore
    S = (2^(n+1) - 2)\phi_0
      = 2(2^n - 1)\phi_0
"""
count = -1  #Totient(1) = 1 but 1/1 is not counted in the set of reduced proper fractions, therefore overcounting is corrected by starting the count at -1.
for bin in bins:
    tot = totient(bin[0])   #tot is \phi_0.
    count += 2*tot
    lb = len(bin[2:])
    count += 2*(2**lb - 1)*tot

for num in odds[halfway:]:
    count += totient(num)

print(count)
