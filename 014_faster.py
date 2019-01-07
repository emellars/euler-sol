#Runtime ~5s.

#Longest Collatz sequence for a starting number under a million using a look-up method which stores some data for previous starting numbers.

def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int(3*n + 1)

max_number=1000000
lookup={}

for n in range(1, max_number):
    collatz_number = n
    count = 0
    while collatz_number != 1:
        if "{}".format(collatz_number) in lookup:
            count += lookup["{}".format(collatz_number)]
            break
        collatz_number = collatz(collatz_number)
        count += 1
    lookup["{}".format(n)] = count

print(max(lookup, key = lookup.get))
