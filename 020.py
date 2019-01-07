#Runtime ~0.07s.

import math

num = math.factorial(100) #num = 100!
num_list = list(map(int, list(str(num)))) #Separate each digit in the evaluated form of 100! and put it into an ordered list.
print(sum(num_list))
