#Runtime ~1.85s.

import math

def number_to_list(n):
    n = str(n)
    return list(map(int, n))

def factorial_sum_check(n):
    n_list = number_to_list(n)
    sum_factorial = sum(map(math.factorial, n_list))
    if n == sum_factorial: return True
    else: return False

#Upper bound is derived by noting that 7 * 9! < 99999999.
special_factorials = [x for x in range(10, 1000000) if factorial_sum_check(x)]
print(sum(special_factorials))
