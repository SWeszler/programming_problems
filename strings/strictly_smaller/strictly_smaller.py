def compare_strings(A, B):
    """This function returns how many strictly smaller strings are in list A for each single string in list B.
    Strictly smaller string is a string that its frequency of occurrences of the smallest character is lower"""
    
    A_strings = A.split(',')
    B_strings = B.split(',')
    a_grouped = {}
    result = []

    for astring in A_strings:
        if astring.count(min(astring)) in a_grouped:
            a_grouped[astring.count(min(astring))] += 1
        else:
            a_grouped[astring.count(min(astring))] = 1

    for bstring in B_strings:
        bcount = bstring.count(min(bstring))
        count = 0
        for i in range(bcount):
            if i in a_grouped:
                count += a_grouped[i]

        result.append(count)

    return result
