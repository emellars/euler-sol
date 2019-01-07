#Runtime ~5.2s.

def check_divisibility(n):
    for d in range(3, 20):
        if n % d != 0: return False
    return True

n = 20
while True:
    if check_divisibility(n):
        break
    else: n += 20
print(n)
