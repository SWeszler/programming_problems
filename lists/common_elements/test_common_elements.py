from unittest import TestCase
from common_elements import common_elements, common_elements_naive

class CommonElementsTest(TestCase):

    def test_01_common_elements(self):
        list_a1 = [1, 3, 4, 6, 7, 9]
        list_a2 = [1, 2, 4, 5, 9, 10]

        self.assertEqual(common_elements(list_a1, list_a2), [1, 4, 9])

    def test_02_common_elements(self):
        list_a1 = [1, 2, 9, 10, 11, 12]
        list_a2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]

        self.assertEqual(common_elements(list_a1, list_a2), [1, 2, 9, 10, 12])

    def test_03_common_elements(self):
        list_a1 = [0, 1, 2, 3, 4, 5]
        list_a2 = [6, 7, 8, 9, 10, 11]

        self.assertEqual(common_elements(list_a1, list_a2), [])

    def test_04_common_elements_time(self):
        list_a1 = []
        list_a2 = []

        for i in range(1000):
            list_a1.append(i)
        for i in range(999, 200000):
            list_a2.append(i)

        self.assertEqual(common_elements(list_a1, list_a2), [999])

    def test_05_common_elements_naive_time(self):
        list_a1 = []
        list_a2 = []

        for i in range(1000):
            list_a1.append(i)
        for i in range(999, 200000):
            list_a2.append(i)

        self.assertEqual(common_elements_naive(list_a1, list_a2), [999])

