#Runtime ~0.07s.

#Define recursive Fibonacci function for postive integer n. Use a dictionary to avoid recalculation of results.
def Fibonacci(n, Fibonacci_dict):
    if "{}".format(n) in Fibonacci_dict:
        return Fibonacci_dict["{}".format(n)]
    else:
        new_number = Fibonacci(n-1, Fibonacci_dict) + Fibonacci(n-2, Fibonacci_dict)
        Fibonacci_dict["{}".format(n)] = new_number
        return new_number

Fibonacci_numbers = {"1" : 1, "2" : 1}
Fibonacci_evens = []

n = 1
#Generate even Fibonacci numbers up to 4 million.
while Fibonacci(n, Fibonacci_numbers) <= 4000000:
    Fn = Fibonacci(n, Fibonacci_numbers)
    if Fn % 2 == 0:
        Fibonacci_evens.append(Fn)
    n += 1

print(sum(Fibonacci_evens))
