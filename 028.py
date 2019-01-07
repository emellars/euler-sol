#Runtime ~1.29s.

import numpy as np

#Fuction necessary to generate an Ulam spiral with odd dimension.
#Order of operations is: right, down, left, up. If the next matrix element is nonzero, then execute the previous operation. For example, if the previous operation was go down, then move one to the left if the left matrix element is zero, otherwise go down again.
def update_indices(matrix, operation, n_index, m_index):
    operator_increment = 0
    #Attempt to go right.
    if operation == 0:
        if matrix[n_index, m_index + 1] == 0:
            m_index += 1
            operator_increment = 1
        else: n_index -= 1
    #Attempt to go down.
    elif operation == 1:
        if matrix[n_index + 1, m_index] == 0:
            n_index += 1
            operator_increment = 1
        else: m_index += 1
    #Attempt to go left.
    elif operation == 2:
        if matrix[n_index, m_index - 1] == 0:
            m_index -= 1
            operator_increment = 1
        else: n_index += 1
    #Attempt to go up.
    elif operation == 3:
        if matrix[n_index - 1, m_index] == 0:
            n_index -= 1
            operator_increment = 1
        else: m_index -= 1
    return n_index, m_index, (operation + operator_increment) % 4

def trace(matrix):
    dim = len(matrix)
    diagonal = []
    for n in range(dim):
        diagonal.append(matrix[n, n])
    return int(sum(diagonal))

def anti_trace(matrix):
    dim = len(matrix)
    anti_diagonal = []
    for n in range(dim):
        anti_diagonal.append(matrix[n, -n-1])
    return int(sum(anti_diagonal))


max_size = 1001    #Size of spiral, must be odd.
ulam = np.zeros((max_size, max_size))   #Initialise the spiral as a matrix of zeroes.

centre = int(max_size/2)
n, m = centre, centre

#Operations [0, 1, 2, 3] correspond to [right, down, left, up], respectively.
current_operation = 0   #Start at 0 since the first move after setting the centre square is to go right.
count = 1
while count <= max_size**2:
    ulam[n, m] = count
    n, m, current_operation = update_indices(ulam, current_operation, n, m)   #Update indices according to the current operation, and also update the next operation to be performed.
    count += 1

print(trace(ulam) + anti_trace(ulam) - 1)
