from unittest import TestCase
from encode_number import encode

class EncodeNumberTest(TestCase):

    def test_01_encode_number(self):
        self.assertEqual(encode(8), "001")

    def test_02_encode_number(self):
        self.assertEqual(encode(23), "1000")

    def test_03_encode_number(self):
        self.assertEqual(encode(107), "101100")