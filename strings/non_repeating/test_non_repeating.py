from unittest import TestCase
from non_repeating import non_repeating

class NonRepeatingStringTest(TestCase):

    def test_01_non_repeating(self):
        self.assertEqual(non_repeating("abcab"), 'c')

    def test_02_non_repeating(self):
        self.assertEqual(non_repeating("abab"), None)

    def test_03_non_repeating(self):
        self.assertEqual(non_repeating("aabbbc"), 'c')

    def test_04_non_repeating(self):
        self.assertEqual(non_repeating("aabbdbc"), 'd')