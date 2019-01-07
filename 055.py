#Runtime ~0.1s.

def palindrome_check(n):
    s = str(n)
    if n == int(s[::-1]): return True
    else: return False

def lychrel_check(n, threshold = 49):
    for z in range(threshold):
        n = n + int(str(n)[::-1])
        if palindrome_check(n): return True
    return False

n = 1
lychrel_count = 9999
while n < 10000:
    if lychrel_check(n): lychrel_count -= 1
    n += 1

print(lychrel_count)
