#Runtime ~4.5s.

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

#Convert number to a list of single digit numbers.
def number_to_list(n):
    n = str(n)
    return list(map(int, n))

#Convert list of single digit numbers to a single number.
def list_to_number(l):
    num = str()
    for elem in l:
        num += str(elem)
    return int(num)

#Cyclically permute a list.
def cyclic_permutation(l):
    return l.insert(0, l.pop())

#Check if n is a circular prime.
def circular_prime_check(n):
    l = number_to_list(n)
    for m in range(len(l) - 1):
        cyclic_permutation(l)
        if prime_check(list_to_number(l)) is False: return False
    return True

circular_candidates = prime_list(999999)
circular_primes = [x for x in circular_candidates if circular_prime_check(x)]
print(len(circular_primes))
