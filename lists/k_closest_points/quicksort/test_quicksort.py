from unittest import TestCase
from quicksort import quicksort

class QuicksortTest(TestCase):

    def test_01_quicksort(self):
        list1 = [2,3,5,1,4,6,7]

        self.assertEqual(quicksort(list1), [1,2,3,4,5,6,7])

    def test_02_quicksort(self):
        list1 = [2,3,5,1,4,7,6,8]

        self.assertEqual(quicksort(list1), [1,2,3,4,5,6,7,8])

    def test_03_quicksort(self):
        list1 = [2]

        self.assertEqual(quicksort(list1), [2])

    def test_04_quicksort(self):
        list1 = [2,3,5,1,4,6,7,9,11,10,8]

        self.assertEqual(quicksort(list1), [1,2,3,4,5,6,7,8,9,10,11])