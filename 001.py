#Runtime ~0.19s.

import numpy as np

#Multiples of 3 and 5 up to 1000.
threes=np.arange(0, 1000, 3)
fives=np.arange(0, 1000, 5)

#Create list of both multiples and delete duplicates.
threes_and_fives = np.unique(np.concatenate((threes, fives)))

#Sum the unique list for answer.
sum_of_multiples = np.sum(threes_and_fives)
print(sum_of_multiples)
