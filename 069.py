#Runtime ~0.07s. See http://mathworld.wolfram.com/TotientFunction.html, where, since \phi(n) = n \prod_{p|n} (1 - 1/p) with the product running over all distinct primes dividing n, n/\phi(n) is maximised when the number of distinct primes (starting from 2 and incrementing) is largest.

def prime_check(cand):
    if cand == 0: return False
    if cand == 1: return False
    for n in range(2, int(cand**(0.5) + 1)):
        if cand % n == 0: return False
    return True

#Largest prime product 2*3*5*7*... before reaching 1000000. 
n, m = 1, 2
while True:
    if prime_check(m):
        next_n = n*m
        if next_n > 1000000: break
        n = next_n
    m += 1
print(n)
