from unittest import TestCase
from expand_mine_sweeper import click

class ExpandMineSweeperTest(TestCase):

    def setUp(self):
        self.field1 = [[0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, -1, 1, 0]]
        self.field2 = [[-1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, -1]]

    def test_01_expand_mine_sweeper(self):
        result = [[0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, -1, 1, 0]]

        self.assertEqual(click(self.field1, 3, 5, 2, 2), result)

    def test_02_expand_mine_sweeper(self):
        result = [[-2, -2, -2, -2, -2],
                [-2, 1, 1, 1, -2],
                [-2, 1, -1, 1, -2]]

        self.assertEqual(click(self.field1, 3, 5, 1, 4), result)

    def test_03_expand_mine_sweeper(self):
        result = [[-1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, -1]]

        self.assertEqual(click(self.field2, 4, 4, 0, 1), result)

    def test_04_expand_mine_sweeper(self):
        result = [[-1, 1, -2, -2],
                [1, 1, -2, -2],
                [-2, -2, 1, 1],
                [-2, -2, 1, -1]]

        self.assertEqual(click(self.field2, 4, 4, 1, 3), result)