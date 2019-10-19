def common_elements(list1, list2):
    """ Returns a list of common elements between list1 and list2 """
    p1 = 0
    p2 = 0
    result = []

    while p1 < len(list1) and p2 < len(list2):
        print(list1[p1], list2[p2])
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        else:
            p1 += 1

    return result



def common_elements_naive(list1, list2):
    """ NAIVE approach, not recommended. Returns a list of common elements between list1 and list2 """
    result = []
    for item1 in list1:
        if item1 in list2:
            result.append(item1)
    return result