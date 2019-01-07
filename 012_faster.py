#Runtime ~3s.

import math

#Returns nth triangle number.
def triangle_number(n):
    return int((1/2)*n*(n + 1))

#Returns number of divisors of a number n by checking factors between 1 and sqrt(n).
def number_of_divisors(n):
    divisors = 0
    ceil_sqrt = math.ceil(math.sqrt(n))
    for k in range(1, ceil_sqrt):
        if n % k == 0: divisors += 2
    if ceil_sqrt == math.sqrt(n): divisors += 1

    return divisors

divisors = 500
count = 0

k = 0
while count < divisors:
    k += 1
    count = number_of_divisors(triangle_number(k))

print(triangle_number(k))
