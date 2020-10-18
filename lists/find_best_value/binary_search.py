def binary_search(arr, target):
    """Iterative Binary Search algorithm, it only works with sorted list.
    Returns index of target value in the list"""

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif target < mid:
            end = mid - 1
        else:
            start = mid + 1

    return False