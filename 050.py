#Runtime ~0.7s.

def prime_check(cand):
    if cand == 0: return False
    if cand == 1: return False
    for n in range(2, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

#Generate the first n prime numbers.
def prime_list(n):
    primes = [2, 3]
    if n == 1: return [2]
    if n == 2: return primes
    cand = 1
    #Prime numbers greater than 3 lie on either 6k - 1 or 6k + 1 for integer k.
    while len(primes) < n:
        x = 6*cand - 1
        y = 6*cand + 1
        if prime_check(x):
            primes.append(x)
        if prime_check(y):
            primes.append(y)
        cand += 1
    if len(primes) == n: return primes
    else: return primes[:-1]

def del_last(l, n):
    new_l = l[:]
    for j in range(n):
        del new_l[-1]
    return new_l

def del_first(l, n):
    new_l = l[:]
    for j in range(n):
        del new_l[0]
    return new_l

#Lower bound on the sum of the first n primes is given by (1/2)(n^2)ln(n). This first exceeds a million for n=563. Therefore the largest number of primes to be checked is 563.
max_prime_index = 563
primes = prime_list(max_prime_index)
max_length = 0

#For a list of 563 sorted primes, drop the first f terms and the last l terms where f + l = m. Compute the sum and check if it is prime. Starting with m = 1 and incrementing in units, the first prime sum found is the maximum.
for m in range(1, max_prime_index):
    for f in range(m + 1):
        for l in range(m + 1):
            if f + l == m:
                truncated_primes = del_first(del_last(primes, l), f)
                truncated_sum = sum(truncated_primes)
                if prime_check(truncated_sum) and truncated_sum < 1000000 and len(truncated_primes) > max_length:
                    max_length = len(truncated_primes)
                    max_consecutive_prime = truncated_sum
                    break
        if max_length !=0: break
    if max_length != 0: break

print(max_consecutive_prime)
