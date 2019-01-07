#Runtime ~1.85s. (Implementation of Narayana's Pandita's algorithm.)

def swap(array, m, n):
    array[m], array[n] = array[n], array[m]

def reverse_end(array, n):
    array[n+1:] = array[n+1:][::-1]

lists = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]  #Start with first list in lexicographic order.
last_list = lists[0][::-1]  #Last list in lexicographic order.
temp = lists[0].copy()

#Generate each list in lexicographic order and stop when last_list has been generated.
while True:
    temp = temp.copy()
    #Find largest n where temp[n+1] > temp[n].
    for n in last_list[1:]:
        if temp[n+1] > temp[n]:
            #Find largest m where m > n and temp[m] > temp[n].
            for m in last_list:
                if temp[m] > temp[n] and m > n:
                    swap(temp, m, n)
                    reverse_end(temp, n)
                    lists.append(temp)
                    break
            break
    #if temp == last_list: break    #Optional line to terminate when all lists permutations have been generated.
    if len(lists) == 1000000: break

print(lists[-1])
