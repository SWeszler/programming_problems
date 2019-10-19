from unittest import TestCase
from is_rotation import is_rotation

class IsRotationTest(TestCase):

    def setUp(self):
        self.list1 = [1, 2, 3, 4, 5, 6, 7]

    def test_is_rotation1(self):
        list2 = [4, 5, 6, 7, 8, 1, 2, 3]
        self.assertEqual(is_rotation(self.list1, list2), False)

    def test_is_rotation2(self):
        list2 = [4, 5, 6, 7, 1, 2, 3]
        self.assertEqual(is_rotation(self.list1, list2), True)

    def test_is_rotation3(self):
        list2 = [4, 5, 6, 9, 1, 2, 3]
        self.assertEqual(is_rotation(self.list1, list2), False)

    def test_is_rotation4(self):
        list2 = [4, 6, 5, 7, 1, 2, 3]
        self.assertEqual(is_rotation(self.list1, list2), False)

    def test_is_rotation5(self):
        list2 = [4, 5, 6, 7, 0, 2, 3]
        self.assertEqual(is_rotation(self.list1, list2), False)

    def test_is_rotation6(self):
        list2 = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(is_rotation(self.list1, list2), True)

    def test_is_rotation7(self):
        list2 = [7, 1, 2, 3, 4, 5, 6]
        self.assertEqual(is_rotation(self.list1, list2), True)

