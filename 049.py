#Runtime ~0.07s.

def prime_sequence_check(cand):
    for m in range(3):
        for n in range(2, int(cand**(0.5) + 1)):
            if cand % n == 0: return False
        cand += 3330
    return True

def number_to_list(n):
    n = str(n)
    return list(map(int, n))

def sequence_permutation(n):
    n1_set = set(number_to_list(n))
    n2_set = set(number_to_list(n + 3330))
    n3_set = set(number_to_list(n + 6660))

    if len(n1_set - n2_set) == 0 and len(n2_set - n3_set) == 0: return True
    else: return False

for n in range(1000, 10000-6660):
    if prime_sequence_check(n) and sequence_permutation(n) and n != 1487:
        print(str(n) + str(n+3330) + str(n+6660))
        break
