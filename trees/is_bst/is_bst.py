class Node:
    """Represents a node in a binary tree"""
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def is_bst(node, lower_lim=None, upper_lim=None):
    """Returns a boolean value True if given binary tree is BST,
     and False if it's not."""

    if lower_lim is not None and node.value < lower_lim:
        return False
    if upper_lim is not None and upper_lim < node.value:
        return False

    is_left_bst = True
    is_right_bst = True
    if node.left:
        is_left_bst = is_bst(node.left, lower_lim, node.value)
    if is_left_bst and node.right:
        is_right_bst = is_bst(node.right, node.value, upper_lim)

    return is_left_bst and is_right_bst
