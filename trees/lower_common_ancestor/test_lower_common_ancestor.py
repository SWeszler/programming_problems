from unittest import TestCase
from lower_common_ancestor import lca, Node

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


class LowerCommonAncestorTest(TestCase):

    def setUp(self):
        self.mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
        self.mapping2 = {5: [1, 4], 1: [3, 8], 4: [9, 2], 3: [6, 7]}
        self.head1 = create_tree(self.mapping1, 0)
        self.head2 = create_tree(self.mapping2, 5)

    def test_01_lca(self):
        self.assertEqual(lca(self.head1, 1, 5), 0)

    def test_02_lca(self):
        self.assertEqual(lca(self.head1, 3, 1), 1)

    def test_03_lca(self):
        self.assertEqual(lca(self.head1, 1, 4), 1)

    def test_04_lca(self):
        self.assertEqual(lca(self.head1, 0, 5), 0)

    def test_05_lca(self):
        self.assertEqual(lca(self.head2, 4, 7), 5)

    def test_06_lca(self):
        self.assertEqual(lca(self.head2, 3, 3), 3)

    def test_07_lca(self):
        self.assertEqual(lca(self.head2, 8, 7), 1)

    def test_08_lca(self):
        self.assertEqual(lca(self.head2, 3, 0), None)