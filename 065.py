#Runtime ~0.07s.

#Gives nth term in sequence [1, 2, 1, 1, 4, 1, 1, 6, 1, ... 1, 2n, 1, ...]
def g(n):
    if n % 3 == 2: return 2*((n+1)//3)
    else: return 1

f = [g(n) for n in range(1, 100)][::-1] #Generate previously mentioned sequence in reverse order up to the 100th convergent.

old_numer = f[0]
old_denom = 1
#Starting from the most nested reciprocal, the continued fraction is built.
for elem in f[1:]:
    #To build the next fraction, the reciprocal of the previous one must be taken (i.e. interchange numerator and denominator.)
    numer = elem*old_numer + old_denom  #Take the reciprocal of the previous fraction and the relevant part of f and combine into a single fraction.
    denom = old_numer
    old_numer, old_denom = numer, denom

#One last reciprocal is taken.
numer = old_denom
denom = old_numer

#Adding the integer part of e to the proper fraction. Take the numerator of this improper fraction.
e_numer = str(numer + 2*denom)
print(sum(map(int, list(e_numer))))
