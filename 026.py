#Runtime ~1.32s.

from mpmath import mp

mp.dps = 2000   #Should be twice as much as the maximum period to be found (since detection of repetition requires at least two repeating units.)

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

#Generate list of prime factors.
def prime_factors(n):
    prime_powers={}
    if prime_check(n):
        prime_powers["{}".format(n)] = 1
        return prime_powers

    for prime in prime_list(int(n/2 + 1)):
        count = 0
        factor_candidate = n
        while True:
            if factor_candidate % prime == 0:
                count += 1
                factor_candidate = factor_candidate / prime
            else:
                if count > 0: prime_powers["{}".format(prime)] = count
                break
    return prime_powers

#Check if reciprocal of n has recurring decimals. (Prime factorisation of 10 is 2*5, so if a a number has a prime factor other than 2 or 5, it will be have a recurring decimal expansion in the reciprocal.)
def recurring_check(n):
    prime_factorisation = prime_factors(n)
    prime_factorisation.pop("2", None)
    prime_factorisation.pop("5", None)

    if len(prime_factorisation) > 0: return True
    else: return False

#Truncate the decimal expansion of a number to mp.dps-2 decimal places.
def truncate(n):
    decimal_places = mp.dps-2
    return mp.floor(n*10**decimal_places) / (10**decimal_places)

#See https://stackoverflow.com/questions/29481088/how-can-i-tell-if-a-string-repeats-itself-in-python/29489919#29489919.
#Check if a rotation of a string is equal to itself and hence extract the period.
def principal_period(s):
    s = s[2:]   #The integer part and decimal period are discarded.
    for n in range(len(s)):
        i = (s+s).find(s, 1, -1)
        if i == -1: s = s[1:]   #Initial part of decimal expansion might not be involved in the periodic part, so remove the first part and repeat.
        else: return len(s[:i])
    return None

denominators = []
recurring_reciprocals = []
#Generate lists of numbers n and 1/n where 1/n has a recurring decimal expansion.
for n in range(3, 1000):
    if recurring_check(n):
        denominators.append(n)
        recurring_reciprocals.append(truncate(1/mp.mpf(n)))

recurring_reciprocals = map(str, recurring_reciprocals)
repeating_periods = list(map(principal_period, recurring_reciprocals))  #Finds period of recurring reciprocals from denominators up to 999.
max_index = repeating_periods.index(max(repeating_periods))

print(denominators[max_index])
