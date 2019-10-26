from unittest import TestCase
from strictly_smaller import compare_strings

class CompareStringsTest(TestCase):

    def test_01_compare_strings(self):
        string1 = "abcd,aabc,bd"
        string2 = "aaa,aa"
        self.assertEqual(compare_strings(string1, string2), [3,2])

    def test_02_compare_strings(self):
        string1 = "abcd,aabc,bd,kjh"
        string2 = "aaa,aa,ccc"
        self.assertEqual(compare_strings(string1, string2), [4,3,4])

    def test_03_compare_strings(self):
        string1 = "ggg,hhh,iii"
        string2 = "a,b,c"
        self.assertEqual(compare_strings(string1, string2), [0,0,0])

    def test_04_compare_strings(self):
        string1 = "cbd"
        string2 = "zaaaz"
        self.assertEqual(compare_strings(string1, string2), [1])