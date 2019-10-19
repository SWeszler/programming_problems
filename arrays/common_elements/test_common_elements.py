from unittest import TestCase
from common_elements import common_elements

class CommonElementsTest(TestCase):

    def test_common_elements1(self):
        list_a1 = [1, 3, 4, 6, 7, 9]
        list_a2 = [1, 2, 4, 5, 9, 10]

        self.assertEqual(common_elements(list_a1, list_a2), [1, 4, 9])

    def test_common_elements2(self):
        list_a1 = [1, 2, 9, 10, 11, 12]
        list_a2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]

        self.assertEqual(common_elements(list_a1, list_a2), [1, 2, 9, 10, 12])

    def test_common_elements3(self):
        list_a1 = [0, 1, 2, 3, 4, 5]
        list_a2 = [6, 7, 8, 9, 10, 11]

        self.assertEqual(common_elements(list_a1, list_a2), [])
