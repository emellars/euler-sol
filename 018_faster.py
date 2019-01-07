#Runtime ~0.067s.

#Converts a list containing numbers in string form to integers.
def string_to_int(list_of_strings):
    return list(map(int, list_of_strings))

triangle_lists = []

with open("018.txt", "r") as triangle_data:
    for line in triangle_data:
        int_list = string_to_int(line.split())
        triangle_lists.append(int_list)

triangle_lists = triangle_lists[::-1]

#Start from the second line from the bottom of the triangle. Add the largest adjacent number from the last line to the corresponding number on the line above and update the list. Iterate until reaching the top of the triangle. The updated number at the top will be the maximum over all paths.
for m in range(len(triangle_lists) - 1):
    for n in range(len(triangle_lists[m + 1])):
        triangle_lists[m + 1][n] += max(triangle_lists[m][n], triangle_lists[m][n+1])

print(triangle_lists[-1][0])
