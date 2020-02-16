
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


def find_best_value(arr, target):
    """Returns the value that after replacing all larger elements in array sum of it would be the closest to given target.
    Sort a list for ease of summation."""
    
    arr.sort()
    arr_len = len(arr)
    lo = min(target//arr_len, arr[0])
    hi = max(target//arr_len, arr[-1])

    def replace_and_sum(arr, arr_len, treshold):
        k = 0
        for item in arr:
            if item > treshold:
                break
            k += 1
        return treshold * (arr_len - k) + sum(arr[:k])

    while lo < (hi - 1):
        mid = (lo + hi) // 2
        arr_sum = replace_and_sum(arr, arr_len, mid)

        if arr_sum == target:
            return mid
        elif arr_sum < target:
            lo = mid
        elif arr_sum > target:
            hi = mid

    low_sum = replace_and_sum(arr, arr_len, lo)
    high_sum = replace_and_sum(arr, arr_len, hi)

    if abs(low_sum - target) <= abs(high_sum - target):
        return lo
    
    return hi