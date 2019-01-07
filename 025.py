#Runtime ~0.125s. (Using Binet's formula would be faster.)
import mpmath

#Define recursive Fibonacci function for postive integer n. Use a dictionary to avoid recalculation of results.
def Fibonacci(n, Fibonacci_dict):
    if "{}".format(n) in Fibonacci_dict:
        return Fibonacci_dict["{}".format(n)]
    else:
        new_number = Fibonacci(n-1, Fibonacci_dict) + Fibonacci(n-2, Fibonacci_dict)
        Fibonacci_dict["{}".format(n)] = new_number
        return new_number

Fibonacci_numbers = {"1" : 1, "2" : 1}

#Note that the ratio between two Fibonacci numbers F_n and F_{n+1} approaches the golden ratio "phi" as n tends to infinity. Hence for F_x >= 10^999, a lower bound on x is derived from \phi^x = 10^999.
phi = (1 + mpmath.sqrt(5))/2
x=int(mpmath.ceil(999 * mpmath.log(10) / mpmath.log(phi)))
print("Lower bound of first Fibonacci index to contain one-thousand digits is", x)

#Increment Fibonacci numbers until one with a thousand digits is found. This will occur for n>=4781.
for n in range(1, 5000):
    Fibonacci(n, Fibonacci_numbers)
    if n >= x and Fibonacci(n, Fibonacci_numbers) >= mpmath.mpf(10**999):
        print("First Fibonacci index to contain one-thousand digits is", n)
        break
