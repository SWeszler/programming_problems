from unittest import TestCase
from knapsack import knapsack

class KnapsackTest(TestCase):

    def test_01_knapsack(self):
        values = [1, 2, 5, 6]
        weights = [2, 3, 4, 5]
        W = 8
        self.assertEqual(knapsack(values, weights, W), 8)

    def test_02_knapsack(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
        self.assertEqual(knapsack(values, weights, W), 220)