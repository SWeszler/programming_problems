def matching_parentheses_nested_for(input):
    """Returns pairs of indices for all matching parentheses 
    or None if at least one doesn't have a match"""
    stack = []
    res = []
   
    for i, c in enumerate(input):
        if c == '(':
            stack.append(i)
            res.append([i])
        elif c == ')':
            if not stack:
                return None
            opening = stack.pop()
            for pair in res:
                if pair[0] == opening:
                    pair.append(i)
                    break
    if stack:
        return None
   
    return res


def matching_parentheses_dict(input):
    """Returns pairs of indices for all matching parentheses 
    or None if at least one doesn't have a match"""
    stack = []
    res = {}
   
    for i, c in enumerate(input):
        if c == '(':
            stack.append(i)
            res[i] = [i]
        elif c == ')':
            if not stack:
                return None
            opening = stack.pop()
            res[opening].append(i)
    if stack:
        return None
   
    return [v for k, v in res.items()]


def matching_parentheses_sort(input):
    """Returns pairs of indices for all matching parentheses 
    or None if at least one doesn't have a match"""
    stack = []
    res = []
   
    for i, c in enumerate(input):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if not stack:
                return None
            opening = stack.pop()
            res.append([opening, i])
    if stack:
        return None

    res.sort()
   
    return res

matching_parentheses = matching_parentheses_sort