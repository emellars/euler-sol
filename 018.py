#Runtime ~2.07s.

import numpy as np

#Converts a list containing numbers in string form to integers.
def string_to_int(list_of_strings):
    return list(map(int, list_of_strings))

#Convert a binary integer less than 2^14 to a list of 0s and 1s with length 14. Then cumulatively sum over that binary list. The resulting list produces an array of indexes which contain every possible path down the triangle.
def binary_to_list(b):
    binary_number = bin(b)
    binary_string_list = list(str(binary_number))[2:]
    binary_list = string_to_int(binary_string_list)
    while len(binary_list) < 14:
        binary_list.insert(0, 0)
    return np.cumsum(binary_list)

triangle_lists = []

with open("018.txt", "r") as triangle_data:
    for line in triangle_data:
        int_list = string_to_int(line.split())
        triangle_lists.append(int_list)

max_total = 0
#Scan over every possible triangle path and record the value of the path with maximum sum.
for m in range(2**14):
    val = 0
    for n in range(1, 15):
        val += triangle_lists[n][binary_to_list(m)[n-1]]
    if val > max_total: max_total = val

print(triangle_lists[0][0] + max_total)
