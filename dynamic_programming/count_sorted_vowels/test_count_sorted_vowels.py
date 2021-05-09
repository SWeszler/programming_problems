from unittest import TestCase
from count_sorted_vowels import count_sorted_vowels_bf, count_sorted_vowels_dp


class CountSortedVowelsTest(TestCase):

    def test_01_count_sorted_vowels_bf(self):
        n = 1
        self.assertEqual(count_sorted_vowels_bf(n), 5)

    def test_02_count_sorted_vowels_bf(self):
        n = 2
        self.assertEqual(count_sorted_vowels_bf(n), 15)

    def test_03_count_sorted_vowels_bf(self):
        n = 5
        self.assertEqual(count_sorted_vowels_bf(n), 126)

    def test_04_count_sorted_vowels_dp(self):
        n = 1
        self.assertEqual(count_sorted_vowels_dp(n), 5)

    def test_05_count_sorted_vowels_dp(self):
        n = 2
        self.assertEqual(count_sorted_vowels_dp(n), 15)

    def test_06_count_sorted_vowels_dp(self):
        n = 5
        self.assertEqual(count_sorted_vowels_dp(n), 126)
