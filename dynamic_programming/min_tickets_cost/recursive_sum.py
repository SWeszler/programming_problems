def recursive_sum(A, i):
    if i >= len(A):
        return 0
    return A[i] + recursive_sum(A, i + 1)


a = [1,2,3,4,5]
t = recursive_sum(a, 0)
print(t)