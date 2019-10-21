class Node:
    """Data structure needed to build a binary tree"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def path_to_x(root, x):
    """Returns a stack representing path to a node in a binary tree"""

    if root is None:
        return None
    if root.value == x:
        return [root]
    left_path = path_to_x(root.left, x)
    if left_path is not None:
        left_path.append(root)
        return left_path
    right_path = path_to_x(root.right, x)
    if right_path is not None:
        right_path.append(root)
        return right_path
    return None


def lca(root, j, k):
    """Returns lowest common ancestor in a binary tree 
    for two given nodes"""

    path_to_j = path_to_x(root, j)
    path_to_k = path_to_x(root, k)

    lca_to_return = None
    while path_to_j and path_to_k:
        j_pop = path_to_j.pop()
        k_pop = path_to_k.pop()
        if j_pop is k_pop:
            lca_to_return = j_pop.value
        else:
            break
    return lca_to_return



def treepath(start):
    """Returns all paths in a tree as a list of strings"""

    if start is None:
        return []
    elif start.left is None and start.right is None:
        return [start.value]
    else:
        result = []
        for l in treepath(start.left) + treepath(start.right):
            result.append(str(start.value) + "," + str(l))
        return result


def lca_naive(root, j, k):
    """NAIVE approach, not recommended.
    Returns lowest common ancestor in a binary tree 
    for two given nodes"""
    
    if j == k:
        return j

    all_paths = treepath(root)

    path_j = []
    path_k = []

    for path in all_paths:
        if str(j) in path:
            path_trim = path.split(str(j))[0] + str(j)
            path_j = path_trim.split(',')
        if str(k) in path:
            path_trim = path.split(str(k))[0] + str(k)
            path_k = path_trim.split(',')

    for x in range(len(path_j) - 1, -1, -1):
        for z in range(len(path_k) - 1, -1, -1):
            if path_j[x] == path_k[z]:
                return int(path_j[x])

    return None
