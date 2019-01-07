#Runtime ~0.7s.

"""
The continuous fraction for sqrt(2) is given by sqrt(2) = 1 + f_\infty, where f_\infty is the proper part of the continuous fraction for sqrt(2).
This proper part may be calculated iteratively: f(1) = 1/2, f(n) = 1/(2 + f(n-1)). Therefore, given that f(n-1) = a/b is known, then f(n) = b/(2b + a).
"""

#This function returns [a, b] where a and b are the numerator and denominator of the proper part of the continuous fraction of sqrt(2), respectively, truncated to n terms.
def f(n, f_dict):
    if "{}".format(n) in f_dict: return f_dict["{}".format(n)]
    else:
        new_val = [f(n - 1, f_dict)[1], 2*f(n - 1, f_dict)[1] + f(n - 1, f_dict)[0]]
        f_dict["{}".format(n)] = new_val
        return new_val

#Gives the numerator and denominator of the continuous fraction of sqrt(2) truncated to n terms.
def sqrt2_cont_frac(n):
    [a, b] = f(n, f_dict)
    return [b + a, b]

f_dict = {"1": [1, 2]}

count = 0
for k in range(1, 1001):
    sqrt2_approx = sqrt2_cont_frac(k)
    if len(str(sqrt2_approx[0])) > len(str(sqrt2_approx[1])): count += 1

print(count)
