def is_rotation(list1, list2):
    """ Returns True if list1 is a rotation of list2 """
    result = True
    if list1[0] not in list2 or len(list1) != len(list2):
        return False
    
    diff = len(list2) - list2.index(list1[0])
    for i in range(len(list1)):
        if list1[i] == list2[i - diff]:
            result &= True
        else:
            result &= False

    return result

