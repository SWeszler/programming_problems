def non_repeating(given_string):
    """Returns the first character from given string that does not appear twice or more"""
    hashtable = {}

    for char in given_string:
        if char in hashtable:
            hashtable[char] += 1
        else:
            hashtable[char] = 1

    for char in given_string:
        if hashtable[char] == 1:
            return char