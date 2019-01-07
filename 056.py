#Runtime ~0.165s.

def digital_sum(n):
    return sum(map(int, str(n)))

maximum = 0
for a in range(2, 100):
    for b in range(2, 100):
        ds = digital_sum(a**b)
        if ds > maximum: maximum = ds

print(maximum)
