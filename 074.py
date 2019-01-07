#Runtime ~5.8s.

#Factorial function with look-up dictionary for previously calculated results.
def factorial(n, dictionary):
    if "{}".format(n) in dictionary: return dictionary["{}".format(n)]
    else:
        n_factorial = n*factorial(n - 1, dictionary)
        dictionary["{}".format(n)] = n_factorial
        return n_factorial

#Returns the length of the factorial chain with starting number n by using a look-up dictionary.
def factorial_chain(n, chain_dict):
    if "{}".format(n) in chain_dict: return chain_dict["{}".format(n)]
    chain = []
    while True: #Begin the factorial chain and stop when a result in the look-up dictionary has been found.
        chain.append(n)
        n, m = map(int, list(str(n))), 0    #Convert n to a list of digits.
        for digit in n:
            m += factorial(digit, fac_dict)
        if "{}".format(m) in chain_dict:    #If a previously calculated result is found, update the dictionary and return the length.
            current_length = len(chain)
            final_length = current_length + chain_dict["{}".format(m)]
            for i in range(current_length):
                chain_dict["{}".format(chain[i])] = final_length - i
            return final_length
        else: n = m

fac_dict = {"0": 1}
chain_dict = {"1": 1, "2": 1, "145": 1, "40585": 1, "169": 3, "363601": 3, "1454": 3, "871": 2, "45361": 2, "872": 2, "45362": 2}   #Values >1 are all possible closed loops and they are given in the problem statement. 1, 2, and 40585 are the only other factorions in addition to 145.

count = 0
for n in range(10**6):
    if factorial_chain(n, chain_dict) == 60: count += 1
print(count)
