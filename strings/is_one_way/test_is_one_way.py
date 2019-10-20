from unittest import TestCase
from is_one_way import is_one_away

class IsOneWayStringTest(TestCase):

    def test_01_is_one_way(self):
        self.assertEqual(is_one_away("abcde", "abcd"), True)

    def test_02_is_one_way(self):
        self.assertEqual(is_one_away("abde", "abcde") , True)

    def test_03_is_one_way(self):
        self.assertEqual(is_one_away("a", "a"), True)

    def test_04_is_one_way(self):
        self.assertEqual(is_one_away("abcdef", "abqdef"), True)

    def test_05_is_one_way(self):
        self.assertEqual(is_one_away("abcdef", "abccef"), True)

    def test_06_is_one_way(self):
        self.assertEqual(is_one_away("abcdef", "abcde"), True)

    def test_07_is_one_way(self):
        self.assertEqual(is_one_away("aaa", "abc"), False)

    def test_08_is_one_way(self):
        self.assertEqual(is_one_away("abcde", "abc"), False)

    def test_09_is_one_way(self):
        self.assertEqual(is_one_away("abc", "abcde"), False)

    def test_10_is_one_way(self):
        self.assertEqual(is_one_away("abc", "bcc"), False)