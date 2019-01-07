#Runtime ~0.065s.

y, count, prev_count = 0, 0, -1
while True:
    x = 1
    while True:
        l = len(str(x**y))
        if l == y: count += 1
        elif l > y: break
        x += 1
    y += 1
    if prev_count == count: break
    else: prev_count = count
    
print(count)
