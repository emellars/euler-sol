#Runtime ~1.42s.

max_number = 10**6
num = list(range(2, max_number + 1))

#Prime sieve method.
for i in range(len(num)):
    if num[i] == i+2:   #If num[i] hasnt been divided, it is prime.
        for j in range(i, len(num), num[i])[1:]:    #For the multiples of num[i] greater than num[i], start implementing the totient product formula.
            num[j] = int(num[j] * (1 - 1/num[i]))
        num[i] = num[i] - 1 #Totient of a prime is the prime minus one.

print(sum(num))
