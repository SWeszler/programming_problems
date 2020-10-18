from unittest import TestCase
from dfs import dfs_acyclic
from bfs import bfs_acyclic
from kahns_top_sort import kahns_top_sort

class TestUtils(TestCase):
    def setUp(self):
        self.graph = {
            0: [1],
            1: [2,3,4],
            2: [4],
            3: [],
            4: []
        }

    def test_01_dfs_acyclic(self):
        expected = [0,1,2,4,3,4]
        self.assertEqual(dfs_acyclic(0, self.graph), expected)

    def test_02_bfs_acyclic(self):
        expected = [0,1,4,3,2,4]
        self.assertEqual(bfs_acyclic(0, self.graph), expected)

    def test_03_kahns_top_sort(self):
        expected = ['01234', '01243', '01324']
        result = kahns_top_sort(self.graph)
        self.assertIn("".join([str(i) for i in result]), expected)

