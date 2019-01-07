#Runtime ~7.7s.

def prime_check(cand):
    for n in range(2, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

#Check if both concatenations of two primes are also prime.
def prime_pair_check(pair):
    pair_str1 = str(pair[0]) + str(pair[1])
    pair_str2 = str(pair[1]) + str(pair[0])
    if prime_check(int(pair_str1)) is False or prime_check(int(pair_str2)) is False: return False
    return True

#For a lexicographical ordering of primes, check all quintuples in lexicographical order---first checking pairs, then triples, then quadruples, and then quintuples.
def prime_quintuple(primes):
    for p1 in primes:
        for p2 in primes:
            if p2 > p1 and prime_pair_check([p1, p2]):
                for p3 in primes:
                    if p3 > p2 and prime_pair_check([p1, p3]) and prime_pair_check([p2, p3]):
                        for p4 in primes:
                            if p4 > p3 and prime_pair_check([p1, p4]) and prime_pair_check([p2, p4]) and prime_pair_check([p3, p4]):
                                for p5 in primes:
                                    if p5 > p4 and prime_pair_check([p1, p5]) and prime_pair_check([p2, p5]) and prime_pair_check([p3, p5]) and prime_pair_check([p4, p5]): return sum([p1, p2, p3, p4, p5])

primes = [3, 7]

#Generate primes up to 10000 (unjustified estimate for an upper bound). Note "5" is skipped as any number ending with 5 is not prime other than 5 itself.
n = 8
while n < 10000:
    if prime_check(n): primes.append(n)
    n += 1

print(prime_quintuple(primes))
