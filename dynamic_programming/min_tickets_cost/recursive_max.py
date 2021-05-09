def recursive_max(A, i):
    if i >= len(A):
        return float('-inf')
    return max(A[i], recursive_max(A, i + 1))


a = [-2,-4,-5,-1]
t = recursive_max(a, 0)
print(t)