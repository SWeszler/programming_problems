from unittest import TestCase
from matching_perentheses import matching_parentheses

class MatchingParenthesesTest(TestCase):

    def test_01_matching_parentheses(self):
        parentheses = "((())()())()"
        result = [[0, 9], [1, 4], [2, 3], [5, 6], [7, 8], [10, 11]]
        self.assertEqual(matching_parentheses(parentheses), result)

    def test_02_matching_parentheses(self):
        parentheses = "((("
        result = None
        self.assertEqual(matching_parentheses(parentheses), result)

    def test_03_matching_parentheses(self):
        parentheses = ")))"
        result = None
        self.assertEqual(matching_parentheses(parentheses), result)

    def test_04_matching_parentheses(self):
        parentheses = "()"
        result = [[0, 1]]
        self.assertEqual(matching_parentheses(parentheses), result)

    def test_05_matching_parentheses(self):
        parentheses = "(("
        result = None
        self.assertEqual(matching_parentheses(parentheses), result)

    def test_06_matching_parentheses(self):
        parentheses = "("
        result = None
        self.assertEqual(matching_parentheses(parentheses), result)

    def test_07_matching_parentheses(self):
        parentheses = "(()"
        result = None
        self.assertEqual(matching_parentheses(parentheses), result)