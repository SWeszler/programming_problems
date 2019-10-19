def most_frequent(given_list):
    """Returns most frequently occurring item from given list"""
    hashtable = {}
    max_count = 0
    result = None

    for i in given_list:
        if i in hashtable:
            hashtable[i] += 1
        else:
            hashtable[i] = 1

        if hashtable[i] > max_count:
            max_count = hashtable[i]
            result = i

    return result

def most_frequent_naive(given_list):
    """NAIVE approach, not recommended. Returns most frequently occurring item from given list"""
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