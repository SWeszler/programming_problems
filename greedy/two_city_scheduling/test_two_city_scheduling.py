from unittest import TestCase
from two_city_scheduling import two_city_scheduling

class TwoCitySchedulingTest(TestCase):

    def test_01_two_city_scheduling(self):
        costs = [[10,20],[30,200],[400,50],[30,20]]
        self.assertEqual(two_city_scheduling(costs), 110)

    def test_02_two_city_scheduling(self):
        costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
        self.assertEqual(two_city_scheduling(costs), 1859)

    def test_03_two_city_scheduling(self):
        costs = [[1,2],[1,2]]
        self.assertEqual(two_city_scheduling(costs), 3)