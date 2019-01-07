#Runtime ~3s.

#Check primality of a number.
def prime_check(cand):
    if cand == 0: return False
    if cand == 1: return False
    for n in range(2, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

#Check if a prime is also a truncatable prime.
def truncatable_prime_check(p):
    p_str = str(p)
    truncate_range = range(1, len(p_str))

    #Left-to-right truncatability.
    for n in truncate_range:
        if prime_check(int(p_str[n:])) == False: return False

    #Right-to-left truncatability.
    for n in truncate_range:
        if prime_check(int(p_str[:n])) == False: return False

    return True

truncatable_primes = []
count = 0
n = 11
while count != 11:
    if prime_check(n) and truncatable_prime_check(n):
        count += 1
        truncatable_primes.append(n)
    n+= 1

print(sum(truncatable_primes))
