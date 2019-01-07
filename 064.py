#Runtime ~4s.

from mpmath import mp

mp.dps = 220

#Finds continued fraction expression for sqrt(n) where the cutoff is the number of decimal places kept record of.
def cont_frac_exp(n, cutoff = 5):
    a, n_history = [], []
    n = mp.sqrt(n)
    a.append(int(n))    #First integer part of the square root continued fraction expansion.
    while True:
        n = 1 / (n - a[-1]) #Form reciprocal and take away the integer part to get 0<n<1.
        if round(n, cutoff) in n_history: break #If n returns to a previously found value, then it will begin to repeat.
        else:
            n_history.append(round(n, cutoff))
            a.append(int(n))
    return a[1:]

count = 0
for n in range(2, 10001):
    m = n**(1/2)
    if m == int(m): continue
    elif len(cont_frac_exp(n)) % 2 == 1: count += 1

print(count)
