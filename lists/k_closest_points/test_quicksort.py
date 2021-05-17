from unittest import TestCase
from quicksort import quicksort_simulation, quicksort


class QuickSortSimulationTest(TestCase):

    def test_01_quicksort_simulation(self):
        list1 = [2, 3, 5, 1, 4, 6, 7]

        self.assertEqual(quicksort_simulation(list1), [1, 2, 3, 4, 5, 6, 7])

    def test_02_quicksort_simulation(self):
        list1 = [2, 3, 5, 1, 4, 7, 6, 8]

        self.assertEqual(quicksort_simulation(list1), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_03_quicksort_simulation(self):
        list1 = [2]

        self.assertEqual(quicksort_simulation(list1), [2])

    def test_04_quicksort_simulation(self):
        list1 = [2, 3, 5, 1, 4, 6, 7, 9, 11, 10, 8]

        self.assertEqual(quicksort_simulation(list1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_05_quicksort_simulation(self):
        list1 = [2, 3, 5, 1, 4, 6, 7, 9, 11, 10, 8]
        list1 = list1 * 100
        sorted_list = quicksort_simulation(list1)

        self.assertEqual(sorted_list[-1], 11)


class QuickSortSimulationForComparisonTest(TestCase):

    def setUp(self):
        import random
        self.arr = [random.randint(0, 1000) for i in range(100000)]

    def test_01_quicksort(self):
        self.arr.append(1000)
        result = quicksort_simulation(self.arr)
        self.assertEqual(result[-1], 1000)


class QuickSortForComparisonTest(TestCase):

    def setUp(self):
        import random
        self.arr = [random.randint(0, 1000) for i in range(100000)]

    def test_01_quicksort(self):
        self.arr.append(1000)
        quicksort(self.arr)
        self.assertEqual(self.arr[-1], 1000)