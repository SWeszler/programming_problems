from unittest import TestCase
from stable_wall import stable_wall

class StableWallTest(TestCase):

    def test_01_stable_wall(self):
        expected = ["ZOAM", "ZOMA"]
        rows = ["ZOAAMM", "ZOAOMM", "ZOOOOM", "ZZZZOM"]
        result = stable_wall(4, 6, rows)
        self.assertIn(result, expected)

    def test_02_stable_wall(self):
        expected = -1
        rows = ["XXOO", "XFFO", "XFXO", "XXXO"]
        result = stable_wall(4, 4, rows)
        self.assertEqual(result, expected)

    def test_03_stable_wall(self):
        expected = -1
        rows = ["XXX", "XPX", "XXX", "XJX", "XXX"]
        result = stable_wall(5, 3, rows)
        self.assertEqual(result, expected)

    def test_04_stable_wall(self):
        expected = ["EDCBA"]
        rows = ["AAABBCCDDE", "AABBCCDDEE", "AABBCCDDEE"]
        result = stable_wall(3, 10, rows)
        self.assertIn(result, expected)