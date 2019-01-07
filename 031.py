#Runtime ~3.9s.

from sympy import *

x = symbols("x")

#Series expansion of f yields a polynomial containing all possible combinations of coins, where the exponent is the total value of the coins and the coefficient is the number of ways to make that total.
f = (1)/((1 - x**200)*(1 - x**100)*(1 - x**50)*(1 - x**20)*(1 - x**10)*(1 - x**5)*(1 - x**2)*(1 - x))
g = f.series(x,0,201)
print(g.coeff(x**200))
