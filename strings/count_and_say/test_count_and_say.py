from unittest import TestCase
from count_and_say import count_and_say

class CountAndSayTest(TestCase):

    def test_01_count_and_say(self):
        self.assertEqual(count_and_say(2), "11")

    def test_02_count_and_say(self):
        self.assertEqual(count_and_say(4), "1211")

    def test_03_count_and_say(self):
        self.assertEqual(count_and_say(6), "312211")

    def test_04_count_and_say(self):
        self.assertEqual(count_and_say(20), "11131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331121321231231121113112221121321133112132112312321123113112221121113122113121113123112112322111213211322211312113211")
