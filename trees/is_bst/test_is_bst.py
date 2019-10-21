from unittest import TestCase
from is_bst import is_bst, Node

def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head

class IsBinarySearchTreeTest(TestCase):

    def setUp(self):
        self.mapping0 = {0: [1, 2]}
        self.mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
        self.mapping2 = {3: [1, 4], 1: [0, 2], 4: [5, 6]}
        self.mapping3 = {3: [1, 5], 1: [0, 2], 5: [4, 6]}
        self.mapping4 = {3: [1, 5], 1: [0, 4]}
        self.head0 = create_tree(self.mapping0, 0)
        self.head1 = create_tree(self.mapping1, 0)
        self.head2 = create_tree(self.mapping2, 3)
        self.head3 = create_tree(self.mapping3, 3)
        self.head4 = create_tree(self.mapping4, 3)

    def test_01_is_bst(self):
        self.assertEqual(is_bst(self.head0), False)

    def test_02_is_bst(self):
        self.assertEqual(is_bst(self.head1), False)

    def test_03_is_bst(self):
        self.assertEqual(is_bst(self.head2), False)

    def test_04_is_bst(self):
        self.assertEqual(is_bst(self.head3), True)

    def test_05_is_bst(self):
        self.assertEqual(is_bst(self.head4), False)
