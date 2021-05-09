def recursive_max(A, i):
    """
    Not using infinity - float('-inf'), returning last item from the list that we assume is max val.
    Recursive function builds a call stack which increments i and gives us the last item first.
    Each result is then compared with A[i].
    """
    if i >= len(A):
        return A[i - 1]
    return max(A[i], recursive_max(A, i + 1))


a = [-2,-4,-5,-1]
t = recursive_max(a, 0)
print(t)