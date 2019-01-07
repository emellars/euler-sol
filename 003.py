#Runtime ~0.07s.

#Check primality of a number.
def prime_check(cand):
    for n in range(2, cand):
        if cand % n == 0: return False
    return True

#Return floor of half of a number.
def half_number(n):
    return int(n/2)

# Return smallest divisor of a number.
def smallest_divisor(n):
    for m in range(2, half_number(n)):
        if n % m == 0:
            return m
    return n

#Return prime factorisation of a number.
factors_list=[]
def divisors(n):
    #If number is prime, append it to the list and return it.
    if n == 1: return factors_list
    elif prime_check(n): return factors_list.append(n)
    #Otherwise append the smallest factor and iterate on the remainder.
    else:
        factor = smallest_divisor(n)
        factors_list.append(factor)
    divisors(int(n/factor))


number = 600851475143

divisors(number)
print(factors_list)
