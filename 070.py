#Runtime ~0.12s.

"""
n/\phi(n) = 1/\prod_{p|n} 1/(1-1/p) as explained in the previous problem. This is minimised when there is only one prime and it is as large as possible. Since \phi(p) = p-1 this cannot be a permutation. Therefore we search for pairs of primes.
Taking some size limit n_max on n, n/\phi(n) looks to be minimised more when pairs of prime factors are taken from the centre (i.e. sqrt(n_max)) rather than the edges (i.e. 2 and the prime less than and nearest to n_max/2). Therefore we search for prime pairs close to sqrt(n).
"""

def prime_check(cand):
    if cand == 0: return False
    if cand == 1: return False
    for n in range(2, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

#Takes two primes p1 and p2 and returns \phi(p1*p2). [\phi(n) = n \prod_p (1-1/p) for prime factors of n (counting repeated primes only once).]
def totient(l):
    p1, p2 = l[0], l[1]
    return int(p1*p2*(1-1/p1)*(1-1/p2))

def mult(l):
    n, m = l[0], l[1]
    return n*m

def permutation_check(n, m):
    n, m = sorted(list(str(n))), sorted(list(str(m)))
    if n == m: return True
    else: return False

#n_max = 10**7 => centre ~ 3000. Search primes in 3000 +- 1000 as a guess.
primes = [n for n in range(2001, 4000, 2) if prime_check(n)]
prime_pairs = [[primes[j], primes[k]] for j in range(len(primes)) for k in range(j, len(primes)) if j != k and primes[j]*primes[k] < 10**7]

numbers = list(map(mult, prime_pairs))
totients = list(map(totient, prime_pairs))

tot_perm_indices = [j for j in range(len(numbers)) if permutation_check(numbers[j], totients[j])]

minimiser = float("inf")
for i in tot_perm_indices:
    cand = numbers[i]/totients[i]
    if cand < minimiser: minimiser, i_max = cand, i

print(numbers[i_max])
