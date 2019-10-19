from unittest import TestCase
from most_frequent import most_frequent, most_frequent_naive

class MostFrequentTest(TestCase):

    def test_01_most_frequent(self):
        given_list = [1, 3, 1, 3, 2, 1]
        self.assertEqual(most_frequent(given_list), 1)

    def test_02_most_frequent(self):
        given_list = [3, 3, 1, 3, 2, 1]
        self.assertEqual(most_frequent(given_list), 3)

    def test_03_most_frequent(self):
        given_list = []
        self.assertEqual(most_frequent(given_list), None)

    def test_04_most_frequent(self):
        given_list = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
        self.assertEqual(most_frequent(given_list), -1)

    def test_05_most_frequent(self):
        given_list = [0]
        self.assertEqual(most_frequent(given_list), 0)

    def test_06_most_frequent_time(self):
        given_list = [5]
        for i in range(10000):
            given_list.append(i)
            
        self.assertEqual(most_frequent(given_list), 5)

    def test_06_most_frequent_time_naive(self):
        given_list = [5]
        for i in range(10000):
            given_list.append(i)
            
        self.assertEqual(most_frequent_naive(given_list), 5)