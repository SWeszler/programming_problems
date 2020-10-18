from unittest import TestCase
from binary_search import binary_search


class BinarySearchTest(TestCase):

    def setUp(self):
        self.bs_arr = [i for i in range(100)]

    def test_01_binary_search(self):
        self.assertEqual(binary_search(self.bs_arr, 34), 34)

    def test_02_binary_search(self):
        self.assertEqual(binary_search(self.bs_arr, 99), 99)

    def test_03_binary_search(self):
        self.assertEqual(binary_search(self.bs_arr, 0), 0)

    def test_04_binary_search(self):
        self.assertEqual(binary_search(self.bs_arr, 102), False)