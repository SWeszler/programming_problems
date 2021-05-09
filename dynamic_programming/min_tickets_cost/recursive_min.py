def recursive_min(A, i):
    if i >= len(A):
        return float('inf')
    return min(A[i], recursive_min(A, i + 1))


a = [1,2,3,6,4,5]
t = recursive_min(a, 0)
print(t)