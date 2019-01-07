#Runtime ~ 4.15s.

#Check primality of a number.
def prime_check(cand):
    if cand <= 0: return False
    for n in range(2, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

min_range, max_range, max_count = -999, 1000, 0

for a in range(min_range, max_range):
    for b in range(min_range - 1, max_range + 1):
        n = 0
        while True:
            if prime_check(n**2 + a*n + b):
                n += 1
            else: break
        if n > max_count:
            max_count = n
            richest_polynomial_product = a*b

print(richest_polynomial_product)
