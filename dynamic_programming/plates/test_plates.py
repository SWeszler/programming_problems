from unittest import TestCase
from plates import plates_bf_itertools, plates_bf, plates_mem, plates_dp

class PlatesTest(TestCase):

    def test_01_plates_bf_itertools(self):
        N, K, P = 2, 4, 5
        stacks = [[10, 10, 100, 30], [80, 50, 10, 50]]
        self.assertEqual(plates_bf_itertools(N, K, P, stacks), 250)

    def test_02_plates_bf_itertools(self):
        N, K, P = 3, 2, 3
        stacks = [[80, 80], [15, 50], [20, 10]]
        self.assertEqual(plates_bf_itertools(N, K, P, stacks), 180)

    def test_03_plates_bf(self):
        N, K, P = 2, 4, 5
        stacks = [[10, 10, 100, 30], [80, 50, 10, 50]]
        self.assertEqual(plates_bf(N, K, P, stacks), 250)

    def test_04_plates_bf(self):
        N, K, P = 3, 2, 3
        stacks = [[80, 80], [15, 50], [20, 10]]
        self.assertEqual(plates_bf(N, K, P, stacks), 180)

    def test_05_plates_mem(self):
        N, K, P = 2, 4, 5
        stacks = [[10, 10, 100, 30], [80, 50, 10, 50]]
        self.assertEqual(plates_mem(N, K, P, stacks), 250)

    def test_06_plates_mem(self):
        N, K, P = 3, 2, 3
        stacks = [[80, 80], [15, 50], [20, 10]]
        self.assertEqual(plates_mem(N, K, P, stacks), 180)

    def test_07_plates_dp(self):
        N, K, P = 2, 4, 5
        stacks = [[10, 10, 100, 30], [80, 50, 10, 50]]
        self.assertEqual(plates_dp(N, K, P, stacks), 250)

    def test_08_plates_dp(self):
        N, K, P = 3, 2, 3
        stacks = [[80, 80], [15, 50], [20, 10]]
        self.assertEqual(plates_dp(N, K, P, stacks), 180)

    def test_09_plates_dp(self):
        N, K, P = 1, 3, 3
        stacks = [[20, 5, 10]]
        self.assertEqual(plates_dp(N, K, P, stacks), 35)