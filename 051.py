#Runtime ~0.27s.

def prime_check(cand):
    if cand == 0: return False
    if cand == 1: return False
    for n in range(2, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

def number_to_list(n):
    n = str(n)
    return list(map(int, n))

def list_to_num(l):
    return int("".join(str(elem) for elem in l))

#Running with only one or two digit replacements does not seem to yield a prime_count > 7.
def prime_digit_replacements(n, i, j, k):
    n = number_to_list(n)
    prime_count = 0
    for digit in range(10):
        m = n[:]
        if digit == 0 and (i == len(m) or j == len(m) or k == len(m)): continue #Ensure that numbers like *x*y*z dont have * = 0 on the leftmost digit. False positives are otherwise encountered.
        m.insert(len(m) - i, digit)
        m.insert(len(m) - j, digit)
        m.insert(len(m) - k, digit)
        m = list_to_num(m)
        if prime_check(m): prime_count += 1
    return prime_count

#Form all possible three digit replacements starting from num = 1 and iterating num up until the eight prime family is found.
max_primes = 0
num = 1
while True:
    num_list = number_to_list(num)
    for i in range(len(num_list) + 1):
        for j in range(len(num_list) + 2):
            for k in range(len(num_list) + 3):
                if j > i and k > j:
                    temp = prime_digit_replacements(num, i, j, k)
                    if temp > max_primes:
                        max_primes = temp
                        min_num = [num, i, j, k]
    if max_primes == 8: break
    else: num += 1

print(min_num)
