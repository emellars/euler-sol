#Runtime ~0.45s.

def number_to_list(n):
    n = str(n)
    return list(map(int, n))

def list_to_num(l):
    return int("".join(str(elem) for elem in l))

def ascending_digits(n):
    return list_to_num(sorted(number_to_list(n)))

def permuted_mult_check(n):
    n_ascending = ascending_digits(n)
    for i in range(2, 7):
        if ascending_digits(i*n) != n_ascending: return False
    return True

x = 1
while True:
    if permuted_mult_check(x):
        print(x)
        break

    x += 1
    #If the first two digits of x are 17 or higher, then multiplying by 6 yields a number with an extra digit. Hence skip to 100 after getting to 17.
    if number_to_list(x)[:2] == [1, 7]:
        x = number_to_list(x)
        x[:2] = [1, 0]
        x.append(0)
        x = list_to_num(x)
