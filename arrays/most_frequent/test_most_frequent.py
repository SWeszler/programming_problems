from unittest import TestCase
from most_frequent import most_frequent

class MostFrequentTest(TestCase):

    def test_most_frequent(self):
        given_list = [1, 3, 1, 3, 2, 1]
        self.assertEqual(most_frequent(given_list), 1)

    def test_most_frequent1(self):
        given_list = [3, 3, 1, 3, 2, 1]
        self.assertEqual(most_frequent(given_list), 3)

    def test_most_frequent2(self):
        given_list = []
        self.assertEqual(most_frequent(given_list), None)

    def test_most_frequent3(self):
        given_list = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
        self.assertEqual(most_frequent(given_list), -1)

    def test_most_frequent4(self):
        given_list = [0]
        self.assertEqual(most_frequent(given_list), 0)