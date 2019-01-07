#Runtime ~3.2s.

#Define recursive Fibonacci function for postive integer n.
def Fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

n = 1
Fibonacci_evens = []
#Generate even Fibonacci numbers up to 4 million.
while Fibonacci(n) <= 4000000:
    Fn = Fibonacci(n)
    if Fn % 2 == 0:
        Fibonacci_evens.append(Fn)
    n += 1

print(sum(Fibonacci_evens))
