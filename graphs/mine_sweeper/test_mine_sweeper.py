from unittest import TestCase
from mine_sweeper import mine_sweeper, mine_sweeper_naive

class MineSweeperTest(TestCase):

    def test_01_mine_sweeper(self):
        bombs = [[0, 2], [2, 0]]
        num_rows = 3
        num_cols = 3
        result = [[0, 1, -1], [1, 2, 1], [-1, 1, 0]]
        self.assertEqual(mine_sweeper(bombs, num_rows, num_cols), result)

    def test_02_mine_sweeper(self):
        bombs = [[0, 0], [0, 1], [1, 2]]
        num_rows = 3
        num_cols = 4
        result = [[-1, -1, 2, 1], [2, 3, -1, 1], [0, 1, 1, 1]]
        self.assertEqual(mine_sweeper(bombs, num_rows, num_cols), result)

    def test_03_mine_sweeper(self):
        bombs = [[1, 1], [1, 2], [2, 2], [4, 3]]
        num_rows = 5
        num_cols = 5
        result = [[1, 2, 2, 1, 0],
                [1, -1, -1, 2, 0],
                [1, 3, -1, 2, 0],
                [0, 1, 2, 2, 1],
                [0, 0, 1, -1, 1]]
        self.assertEqual(mine_sweeper(bombs, num_rows, num_cols), result)

    def test_04_mine_sweeper_naive(self):
        bombs = [[1, 1], [1, 2], [2, 2], [4, 3]]
        num_rows = 5
        num_cols = 5
        result = [[1, 2, 2, 1, 0],
                [1, -1, -1, 2, 0],
                [1, 3, -1, 2, 0],
                [0, 1, 2, 2, 1],
                [0, 0, 1, -1, 1]]
        self.assertEqual(mine_sweeper_naive(bombs, num_rows, num_cols), result)