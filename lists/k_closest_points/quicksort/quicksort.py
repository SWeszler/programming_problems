def quicksort(sequence):
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


    return quicksort(items_lower) + [pivot] + quicksort(items_higher)


def quicksort_2(sequence):
    if len(sequence) <= 1:
        return sequence

    def partition(lo, hi):
        pivot = sequence[0]

        while(lo < hi):
            while sequence[lo] <= pivot:
                lo += 1
            while sequence[hi] > pivot:
                hi += 1

            
