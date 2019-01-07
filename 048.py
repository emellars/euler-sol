#Runtime ~0.07s.

value = 0
for n in range(1,1001):
    value += n**n

print(str(value)[-10:])
