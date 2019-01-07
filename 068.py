#Runtime ~14s.

import itertools as iter

#Given a list l, return numbers at indices l_n.
def list_select(l, l_n):
    return [[l[n] for n in l_n]]

sum_targets = [14, 16, 17]  #Solutions only exist for these sums.
seqs = [sublist for sublist in list(iter.permutations(range(1,11))) if all(sl > sublist[0] for sl in [sublist[2], sublist[4], sublist[6], sublist[8]])]    #Retain only sequences which generate valid 5-gons (i.e. starting with numerically lowest external node).

five_gons = [[l1, l2, l3, l4, l5] for sum_target in sum_targets for sublist in seqs for l1, l2, l3, l4, l5 in zip(list_select(sublist, [0, 9, 1]), list_select(sublist, [2, 1, 3]), list_select(sublist, [4, 3, 5]), list_select(sublist, [6, 5, 7]), list_select(sublist, [8, 7, 9])) for l in [l1, l2, l3, l4, l5] if all(sum(l) == sum_target for l in [l1, l2, l3, l4, l5])]    #Generate all valid 5-gons.

five_gon_strings = []
for sublist in five_gons:
    s = ""
    for nested_sublist in sublist:
        for n in nested_sublist:
            s = s + str(n)
    if len(s) == 16: five_gon_strings.append(s)

print(max(five_gon_strings))
