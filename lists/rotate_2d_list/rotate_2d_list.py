import copy
from math import floor, ceil

def rotate(given_array, n):
    rotated = copy.deepcopy(given_array)
    j = n - 1
    for row in given_array:
        i = 0
        for val in row:
            rotated[i][j] = val
            i += 1
        j -= 1

    return rotated

def new_pos(i, j, n):
    return j, n - 1 - i

def rotate_graph_in_place(given_array, n):
    for i in range(int(floor(float(n)/2))):
        for j in range(int(ceil(float(n)/2))): # n must be converted to float for Python 2.x
            tmp = [-1, -1, -1, -1]
            current_i, current_j = i, j
            for k in range(4):
                tmp[k] = given_array[current_i][current_j]
                current_i, current_j = new_pos(current_i, current_j, n)
            for k in range(4):
                given_array[current_i][current_j] = tmp[(k + 3) % 4] # rotating list indexes
                current_i, current_j = new_pos(current_i, current_j, n)

    return given_array
