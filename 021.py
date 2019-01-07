#Runtime ~0.12s.

import math

#Returns divisors of a number n by checking factors between 1 and sqrt(n).
def divisors(n):
    divisors_list = []
    ceil_sqrt = math.ceil(math.sqrt(n))
    for k in range(1, ceil_sqrt):
        if n % k == 0:
            divisors_list.append(k)
            if k != 1: divisors_list.append(int(n/k))
    if ceil_sqrt == math.sqrt(n): divisors_list.append(ceil_sqrt)
    return sorted(divisors_list)

max_number = 10000
amicable_candidates = []

#Generate a list containing sums of divisors up to max_number.
for n in range(max_number):
    amicable_candidates.append(sum(divisors(n)))

amicable_numbers = []

#Check the list of the sums of divisors for amicable numbers, i.e. for the amicable function a: a(a(n)) = n where n<max_number and a(n) != n.
for n in range(max_number):
    if amicable_candidates[n] < max_number and amicable_candidates[amicable_candidates[n]] == n and amicable_candidates[n] != n:
        amicable_numbers.append(n)

print(sum(amicable_numbers))
