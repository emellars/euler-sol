#Runtime ~3.6s.

import math

max_number = 12000

count = -1  #Start count at -1 since the loop below counts 1/3 which is to be discounted. (i.e. for d=3, the range of n is range(1, 2) so that 1/3 is sampled.)
for d in range(2, max_number + 1):
    for n in range(math.ceil(d/3), math.ceil(d/2)):
        if math.gcd(d, n) == 1: count += 1

print(count)
