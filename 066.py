#Runtime ~0.25s. Using the continued fraction method to solve Pell's equation (see http://mathworld.wolfram.com/PellEquation.html).

from mpmath import mp
mp.dps = 100

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
    return a

#Returns the fundamental solution [x, y, D] for the Diophantine equation for a given D.
def Diophantine_solution(D):
    f = cont_frac_exp(D)
    integer_part = f[0]

    #If the continued fraction contains only one reciprocal, return the answer immediately. Otherwise, take a truncated form of the improper fraction.
    if len(f) == 2: return [1 + integer_part*f[1], f[1], D]
    #If the period is even, truncate to the end of the first period.
    elif len(f[1:]) % 2 == 0: f = f[1:-1][::-1]
    #If the period is odd, truncate to the end of the second period.
    else:
        f = f[1:]
        f.extend(f)
        f = f[:-1][::-1]

    old_numer = f[0]
    old_denom = 1
    #Starting from the most nested reciprocal, the continued fraction is built.
    if len(f) > 1:
        for elem in f[1:]:
            #To build the next fraction, the reciprocal of the previous one must be taken (i.e. interchange numerator and denominator.)
            numer = elem*old_numer + old_denom  #Take the reciprocal of the previous fraction and the relevant part of f and combine into a single fraction.
            denom = old_numer
            old_numer, old_denom = numer, denom
    else: numer, denom = old_numer, old_denom

    #One last reciprocal is taken.
    numer = old_denom
    denom = old_numer

    #Adding the integer part back to the proper fraction. Return the numerator of this improper fraction, which is x of the fundamental solution to the Diophantine equation with constant D.
    full_numer = numer + integer_part*denom
    return [full_numer, denom, D]

D_range = [D for D in range(1, 1001) if D**(1/2) != D**(1/2)//1]

max = 0
for D in D_range:
    x_sol = Diophantine_solution(D)[0]
    if x_sol > max: max, D_sol = x_sol, D

print(D_sol)
