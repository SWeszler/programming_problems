def matching_parentheses(input):
    """Returns pairs of indices for all matching parentheses 
    or None if at least one doesn't have a match"""
    
    if len(input) < 2 or '(' != input[0]:
        return None

    find_matching = []
    result = []
   
    for i in range(len(input)):
        find_matching.append([input[i], i])
        if input[i] == ')' and find_matching[len(find_matching) - 2][0] == '(':
            find_matching.pop()
            to_result = find_matching.pop()
            result.append([to_result[1], i])
   
    if find_matching:
        return None

    result.sort()
   
    return result


      
	


