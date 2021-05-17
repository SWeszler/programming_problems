def quicksort_simulation(sequence):
    """
    This is not really a Quick Sort.
    It's not in-place and time complexity isn't O(NlogN), there's additional O(N) for list concatenation.
    Also, it's not practical, recursion will not work form more than a 1000 item array.
    This is only to understand how Divide and Conquer approach works.
    """
    if len(sequence) <= 1:
        return sequence

    pivot = sequence.pop()

    items_lower = []
    items_higher = []

    for item in sequence:
        if item > pivot:
            items_higher.append(item)
        else:
            items_lower.append(item)

    return quicksort_simulation(items_lower) + [pivot] + quicksort_simulation(items_higher)


def quicksort_recursive(A, l=0, r=None):
    if r is None:
        r = len(A) - 1

    if l >= r:
        return

    i, j = l, r
    pivot = A[l]

    while i <= j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1

        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    quicksort_recursive(A, l, j)
    quicksort_recursive(A, i, r)



def quicksort(A):

    def partition(arr, l, r):
        import random 
        i, j = l, r
        pivot = arr[random.randint(l, r)]
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1

            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        return i, j
    
    left = 0
    right = len(A) - 1
    stack = [(left, right)]
  
    while stack:
        left, right = stack.pop()
        i, j = partition(A, left, right)
        if j > left:
            stack.append((left, j))
        if i > right:
            stack.append((right, i))
