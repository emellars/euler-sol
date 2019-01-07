#Runtime ~4s.

max_number = 2*10**6
num, flags = list(range(2, max_number + 1)), [1]*(max_number - 1)

#Prime sieve method.
for i in range(len(num)):
    if num[i] == i+2:   #If num[i] hasnt been divided, it is prime.
        for j in range(i, len(num), num[i])[1:]:
            flags[j] = 0

primes = [n for n, f in zip(num, flags) if f != 0]
print(sum(primes))
