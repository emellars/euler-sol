#Runtime ~s. (See: https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple.)

import math

max_number = 1000

def triple(k, m, n):
    a = k*(m**2 - n**2)
    b = k*(2*m*n)
    c = k*(m**2 + n**2)
    return a+b+c

#perims = sorted([triple(k, m, n) for k in range(1, 400) for n in range(1, 400) for m in range(1, 400) if m > n and math.gcd(m, n) == 1 and (m % 2 == 0 or n % 2 == 0) and triple(k, m, n) < 1500000])

perims = []
for m in range(1, 100):
    for n in range(1, 100):
        k = 1
        while True:
            t = triple(k, m, n)
            if t > 1500000: break
            else:
                perims.append(t)
                k += 1

print(len(perims))  #1800: 23127168, 2000: 23590728, 3000: 25324653
