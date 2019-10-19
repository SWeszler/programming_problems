def most_frequent(given_list):
    """Returns most frequently occurring item from given list"""
    max_item = None
    
    max_count = 0
    for el in given_list:
        i = 0
        for el1 in given_list:
            if el == el1:
                i += 1
            if i > max_count:
                max_count = i
                max_item = el

        
    return max_item