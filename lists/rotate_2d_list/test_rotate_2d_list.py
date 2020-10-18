from unittest import TestCase
from rotate_2d_list import rotate, rotate_graph_in_place

class Rotate2DListTest(TestCase):

    def test_01_rotate_2d_list(self):
        a1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
        result = [[7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]]

        self.assertEqual(rotate(a1, 3), result)

    def test_02_rotate_2d_list(self):
        a2 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

        result = [[13, 9, 5, 1],
                [14, 10, 6, 2],
                [15, 11, 7, 3],
                [16, 12, 8, 4]]

        self.assertEqual(rotate(a2, 4), result)

    def test_03_rotate_2d_list(self):
        a1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
        result = [[7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]]

        self.assertEqual(rotate_graph_in_place(a1, 3), result)

    def test_04_rotate_2d_list(self):
        a2 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

        result = [[13, 9, 5, 1],
                [14, 10, 6, 2],
                [15, 11, 7, 3],
                [16, 12, 8, 4]]

        self.assertEqual(rotate_graph_in_place(a2, 4), result)