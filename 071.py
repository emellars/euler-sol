#Runtime ~1.15s.

import math
import numpy as np

#For a denominator d, the nearest value to 3/7 which is less than 3/7 is the floor of (3/7)d.
proper_fractions = np.array([[math.floor((3/7)*d),d] for d in range(2, 10**6 + 1) if math.gcd(math.floor((3/7)*d), d) == 1])
#Convert fractions to floats and get the indices that sort them.
floats = np.array([frac[0]/frac[1] for frac in proper_fractions])

#The largest number is 3/7. Hence sort and find the number to the left of it.
ordered_fractions = proper_fractions[np.argsort(floats)]
print(ordered_fractions[-2:])
