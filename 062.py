#Runtime ~0.08s.

from collections import Counter
import math

#Calculate cubes with j digits and convert each to a string. Sort each cube and count frequency of the sorted cubes to get the number of cubic permutations.
i, j, max_number = 0, 1, 1
while max_number != 5:
    i += 1
    j += 1

    #j-digit numbers fall between these two values.
    cube_min_index = math.ceil(10**(i/3))
    cube_max_index = math.ceil(10**(j/3))

    #Generate cubes as strings and sort each one.
    cubes = [str(n**3) for n in range(cube_min_index, cube_max_index)]
    sorted_cubes = map(sorted, cubes)
    sorted_cubes = ["".join(elem) for elem in sorted_cubes]

    #Count frequency of sorted cubes.
    cube_freq_dict = Counter(sorted_cubes)
    max_number = max(list(cube_freq_dict.values()))

#Find all possible sequences with the required frequency.
answer_sequence, matching_sequences = 0, []
for k, v in cube_freq_dict.items():
    if v == max_number and answer_sequence != k:
        answer_sequence = k
        matching_sequences.append(answer_sequence)

#Select the valid sequence with the minimum cube.
answer_indices = [sorted_cubes.index(sequence) for sequence in matching_sequences]
answers = [cubes[index] for index in answer_indices]
print(min(answers))
