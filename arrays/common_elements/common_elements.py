def common_elements(list1, list2):
    result = []
    for item1 in list1:
        if item1 in list2:
            result.append(item1)
    return result