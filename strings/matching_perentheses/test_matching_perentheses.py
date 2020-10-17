from unittest import TestCase
from matching_perentheses import matching_parentheses

class MatchingParenthesesTest(TestCase):

    def test_01_matching_parentheses(self):
        parentheses = "((())()())()"
        expected = [[0, 9], [1, 4], [2, 3], [5, 6], [7, 8], [10, 11]]
        self.assertEqual(matching_parentheses(parentheses), expected)

    def test_02_matching_parentheses(self):
        parentheses = "((("
        expected = None
        self.assertEqual(matching_parentheses(parentheses), expected)

    def test_03_matching_parentheses(self):
        parentheses = ")))"
        expected = None
        self.assertEqual(matching_parentheses(parentheses), expected)

    def test_04_matching_parentheses(self):
        parentheses = "()"
        expected = [[0, 1]]
        self.assertEqual(matching_parentheses(parentheses), expected)

    def test_05_matching_parentheses(self):
        parentheses = "(("
        expected = None
        self.assertEqual(matching_parentheses(parentheses), expected)

    def test_06_matching_parentheses(self):
        parentheses = "("
        expected = None
        self.assertEqual(matching_parentheses(parentheses), expected)

    def test_07_matching_parentheses(self):
        parentheses = "(()"
        expected = None
        self.assertEqual(matching_parentheses(parentheses), expected)


class MatchingParenthesesLargeInputTest(TestCase):

    def setUp(self):
        N = 10**6
        self.input = "(" * N + ")" * N
        self.expected = []
        for i in range(N):
            self.expected.append([i, 2*N - i - 1])

    def test_01_matching_parentheses(self):
        result = matching_parentheses(self.input)
        self.assertEqual(result, self.expected)