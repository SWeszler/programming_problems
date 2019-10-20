from unittest import TestCase
from nth_from_last import nth_from_last, Node

class NthElementOfLinkedListTest(TestCase):

    def setUp(self):
        current = Node(1)
        for i in range(2, 8):
            current = Node(i, current)
        self.head = current

        current2 = Node(4)
        for i in range(3, 0, -1):
            current2 = Node(i, current2)
        self.head2 = current2

    def test_01_nth_from_last(self):
        self.assertEqual(nth_from_last(self.head, 1), '1')

    def test_02_nth_from_last(self):
        self.assertEqual(nth_from_last(self.head, 5), '5')

    def test_03_nth_from_last(self):
        self.assertEqual(nth_from_last(self.head2, 2), '3')

    def test_04_nth_from_last(self):
        self.assertEqual(nth_from_last(self.head2, 4), '1')

    def test_05_nth_from_last(self):
        self.assertEqual(nth_from_last(self.head2, 5), None)

    def test_06_nth_from_last(self):
        self.assertEqual(nth_from_last(None, 1), None)
