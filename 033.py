#Runtime ~0.2s.

import numpy as np

cancelling_numerators = []
cancelling_denominators = []

#Check all combinations and retain nontrivial cancelling fractions.
for numerator in range(10,100):
    for denominator in range(10,100):
        if str(numerator)[1] == str(denominator)[0] and str(denominator)[1] != "0" and denominator > numerator:
            new_numerator, new_denominator = int(str(numerator)[0]), int(str(denominator)[1])
            if numerator/denominator == new_numerator/new_denominator:
                cancelling_numerators.append(numerator)
                cancelling_denominators.append(denominator)

prod_num = np.prod(cancelling_numerators)
prod_denom = np.prod(cancelling_denominators)

print(prod_denom / prod_num)
