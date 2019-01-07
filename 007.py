#Runtime ~0.2s.

#Check primality of an odd number.
def prime_check(cand):
    for n in range(3, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

#Generate the first n prime numbers.
def prime_list(n):
    list = [2] #Start with the first prime for convenience (since it is even).
    if n == 1: return list
    cand = 3 #Number to be tested for primality.
    prime_count = 1 #Number of primes found.
    while prime_count < n:
        if prime_check(cand):
            list.append(cand)
            prime_count+=1
        cand+=2
    return list

print(prime_list(10001)[-1])
