#Runtime ~9.2s.

#Check primality of an odd number.
def prime_check(cand):
    for n in range(3, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

#Generate all prime numbers below n.
def prime_list(n):
    primes = [2, 3]
    if n == 1: return primes[1]
    if n == 2: return primes
    cand = 1
    #Prime numbers greater than 3 lie on either 6k - 1 or 6k + 1 for integer k.
    while 6*cand + 1 < n:
        x = 6*cand - 1
        y = 6*cand + 1
        if prime_check(x):
            primes.append(x)
        if prime_check(y):
            primes.append(y)
        cand += 1
    return primes

print(sum(prime_list(2000000)))
