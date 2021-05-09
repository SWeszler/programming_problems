class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

root = Node(4)
root.left = Node(1)
root.right = Node(12)
root.right.left = Node(6)
root.right.right = Node(4)
root.right.left.left = Node(2)
root.right.left.right = Node(3)


def in_order(node):
    s = 0
    if not node:
        return s
    
    s += in_order(node.left)
    if node.left is None and node.right is None:
        print(node.value)
    if node.left is not None and node.right is not None:
        s += node.value
    s += in_order(node.right)

    return s

s = in_order(root)
print('sum', s)

root1 = Node(8)
root1.left = Node(2)
root1.right = Node(12)
root1.left.left = Node(1)
root1.left.right = Node(2)
root1.right.left = Node(3)
root1.right.right = Node(4)

s = in_order(root1)
print('sum', s)

root2 = Node(8, Node(2, Node(1), Node(2)), Node(12, Node(3), Node(4)))

s = in_order(root2)
print('sum', s)