from unittest import TestCase
from k_closest_points import k_closest_points, quicksort

class KClosestPointsTest(TestCase):

    def test_01_k_closest_points(self):
        points = [[1,3],[-2,2]]
        K = 1
        result = [[-2,2]]

        self.assertEqual(k_closest_points(points, K), result)

    def test_02_k_closest_points(self):
        points = [[3,3],[5,-1],[-2,4]]
        K = 2
        result = [[-2,4],[3,3]]

        self.assertCountEqual(k_closest_points(points, K), result)
