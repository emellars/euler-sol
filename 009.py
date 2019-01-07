#Runtime ~0.36s. (Note: see 039.py for a faster way to generate Pythagorean triples.)

import numpy as np

#Takes list [a, b, c] and checks if a^2 + b^2 == c^2.
def pythagoras(triplet):
    return triplet[0]**2 + triplet[1]**2 - triplet[2]**2 == 0

triplets = []

#Generate all possible triples [a, b, c] where a<b<c.
for a in range (1, 333):
    for b in range (a + 1, 500):
            c = 1000 - a - b
            if c > b:
                triplets.append([a, b, c])

#Check all possible triples to see if they are Pythagorean triples.
pythagoras_check = map(pythagoras, triplets)
pythagoras_bools = np.array(list(map(int, pythagoras_check)))

#Select the single Pythagorean triple and calculate its product.
triplets = np.array(triplets)
pythagorean_triplet = np.matmul(pythagoras_bools, triplets)
print(np.prod(pythagorean_triplet))
