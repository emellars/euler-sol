#Runtime ~34s.

#Brute force method to find maximum Collatz length for starting numbers not exceeding a given maximum.

def collatz(n, count = 1):
    if n == 1: return count
    count += 1
    if n % 2 == 0:
        return collatz(n/2, count)
    else:
        return collatz(3*n + 1, count)

max_number = 1000000
starting_numbers = [1] + list(range(1, max_number))
collatz_lengths = list(map(collatz, starting_numbers))
max_length = max(collatz_lengths)

for i in range(max_number):
    if collatz_lengths[i] == max_length:
        print(list(enumerate(collatz_lengths))[i])
