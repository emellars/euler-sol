#Runtime ~0.2s.

import fnmatch
import itertools as iter

#For two lists of numbers, return a list of cyclic pairs between them (i.e. for some elements elem1 in list1 and elem2 in list2, the pair [elem1, elem2] is cyclic iff elem1[2:] == elem2[:2]).
#Note that list1 can contain sublists, and only the number at the end of the sublist is used for cyclic comparisons.
def find_cyclics(list1, list2):
    cyclics = []
    for elem1 in list1:
        if type(elem1) == list: new_elem = elem1[-1]    #Only compare the last element of list1 with elements of list2.
        else:
            new_elem = elem1
            elem1 = [elem1]
        filtered_list = fnmatch.filter(list2, new_elem[2:] + "*")
        if len(filtered_list) > 0: cyclics.extend(elem1 + [elem2] for elem2 in filtered_list)
    return cyclics

#Polygonal numbers.
def P(m, n):
    if m == 3:
        return n*(n+1)//2   #\in [1000,10000) for n \in [45, 140].
    elif m == 4:
        return n**2         #\in [1000,10000) for n \in [32, 99]
    elif m == 5:
        return n*(3*n-1)//2 #\in [1000,10000) for n \in [26, 81]
    elif m == 6:
        return n*(2*n-1)    #\in [1000,10000) for n \in [23, 70]
    elif m == 7:
        return n*(5*n-3)//2 #\in [1000,10000) for n \in [21, 63]
    elif m == 8:
        return n*(3*n-2)    #\in [1000,10000) for n \in [19, 58]
    else: return "Only enter integer 3<=m<=8."

triangles = [str(P(3, n)) for n in range(45, 141)]
quads = [str(P(4, n)) for n in range(32, 100)]
pentagons = [str(P(5, n)) for n in range(26, 82)]
hexagons = [str(P(6, n)) for n in range(23, 71)]
septagons = [str(P(7, n)) for n in range(21, 64)]
octagons = [str(P(8, n)) for n in range(19, 59)]

polygonals = [octagons, septagons, hexagons, pentagons, quads, triangles]

polygonal_orderings = iter.permutations(polygonals) #Generate all possible orderings for the linked cyclic numbers (e.g., first one tried is octagon->septagon->hexagon->pentagon->quad->triangle).

finished = 0
for sublist in polygonal_orderings:
    #Find cyclic pairs between adjacent sublists.
    cyclic_01 = find_cyclics(sublist[0], sublist[1])
    cyclic_012 = find_cyclics(cyclic_01, sublist[2])
    cyclic_0123 = find_cyclics(cyclic_012, sublist[3])
    cyclic_01234 = find_cyclics(cyclic_0123, sublist[4])
    cyclic_012345 = find_cyclics(cyclic_01234, sublist[5])
    #Check that the last number connects cyclically to the first.
    for sublist in cyclic_012345:
        if sublist[-1][2:] == sublist[0][:2]:
            print(sum(map(int, sublist)))
            finished = 1
            break
    if finished == 1: break
