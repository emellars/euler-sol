#Runtime ~0.65s.

def factorial(n, dictionary):
    if "{}".format(n) in dictionary: return dictionary["{}".format(n)]
    else:
        n_factorial = n*factorial(n - 1, dictionary)
        dictionary["{}".format(n)] = n_factorial
        return n_factorial

def choose(n, r, dictionary):
    return int(factorial(n, dictionary)//(factorial(r, dictionary)*factorial(n - r, dictionary)))

fac_dict = {"0": 1}

#Count number of "n choose r" values that are below a million. Using the symmetry of the choose function, infer the number of values above a million.
count_supermillion = 0  #Tracks number of values > 1000000 for 1 <= n <= 100.
for n in range(1, 101):
    count_submillion = 0    #Tracks number of values < 1000000 for a particular value of n.
    for r in range(n//2):
        if choose(n, r, fac_dict) > 1000000:
            count_supermillion += n + 1 - 2*count_submillion    #For a fixed value of n, there are n + 1 values of r (i.e. r \in [0, 1, 2, ..., n]) and the choose function is symmetric about r=n/2, where it monotonically increases towards this centre.
            break
        else: count_submillion += 1

print(count_supermillion)
