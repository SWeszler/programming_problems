def the_same_length(s1, s2):
    """Returns True if given strings are one way from each other, 
    which means there's only one change that needs to be made to make both strings the same.
    
    Given strings must have the same length.
    """
    count_diff = 0
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count_diff += 1

        if count_diff > 1:
            return False

    return True


def diff_length(s1, s2):
    """Returns True if given strings are one way from each other, 
    which means there's only one change that needs to be made to make both strings the same.
    
    Length difference must not be greater than one.
    """

    count_diff = 0
    
    for i in range(len(s1)):
        if s1[i] != s2[(i + count_diff) % len(s2)]:
            count_diff += 1
        
        if count_diff > 1:
            return False

    return True

def is_one_away(s1, s2):
    """Returns True if given strings are one way from each other, 
    which means there's only one change that needs to be made to make both strings the same"""

    if abs(len(s1) - len(s2)) > 1:
        return False
    elif len(s1) == len(s2):
        return the_same_length(s1,s2)
    else:
        return diff_length(s1, s2)

    return True
