#Runtime ~26.5s.

import math

#Takes list [a, b, c] and checks if a^2 + b^2 == c^2.
def pythagoras(triplet):
    return triplet[0]**2 + triplet[1]**2 - triplet[2]**2 == 0

#Generate all pythagorean triples [a, b, c] where a>b>c, a+b+c=p.
def triplets(p):
    triples = []
    for a in range(1, math.floor(p/3)):
        for b in range(a + 1, math.floor(p/2)):
            c = p - a - b
            if c > b and a**2 + b**2 == c**2: triples.append([a, b ,c])
    return triples


max_number_of_solutions = 3
p_max = 120

for p in range(120, 1001):
    triples = triplets(p)
    if len(triples) <= max_number_of_solutions: continue
    else:
        max_number_of_solutions = len(triples)
        p_max = p

print("Maximum number of solutions is {} and occurs for p = {}.".format(max_number_of_solutions, p_max))
