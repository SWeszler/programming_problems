from unittest import TestCase
from alien_piano import alien_piano_bf, alien_piano_mem, alien_piano_dp, alien_piano


class AlienPianoTest(TestCase):

    def test_01_alien_piano_K5(self):
        K = 5
        notes = [1, 5, 100, 500, 1]
        self.assertEqual(alien_piano(K, notes), 0)

    def test_02_alien_piano_K8(self):
        K = 8
        notes = [2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(alien_piano(K, notes), 1)

    def test_03_alien_piano_K13(self):
        K = 13
        notes = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5]
        self.assertEqual(alien_piano(K, notes), 0)

    def test_04_alien_piano_K10000(self):
        K = 10000
        notes = [n for n in range(K)]
        self.assertEqual(alien_piano(K, notes), 2499)


class AlienPianoBFTest(TestCase):

    def test_01_alien_piano_bf_K5(self):
        K = 5
        notes = [1, 5, 100, 500, 1]
        self.assertEqual(alien_piano_bf(K, notes), 0)

    def test_02_alien_piano_bf_K8(self):
        K = 8
        notes = [2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(alien_piano_bf(K, notes), 1)

    def test_03_alien_piano_bf_K10(self):
        K = 10
        notes = [n for n in range(K)]
        self.assertEqual(alien_piano_bf(K, notes), 2)

    def test_04_alien_piano_bf_K13(self):
        K = 13
        notes = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5]
        self.assertEqual(alien_piano_bf(K, notes), 0)


class AlienPianoMemTest(TestCase):

    def test_01_alien_piano_mem_K5(self):
        K = 5
        notes = [1, 5, 100, 500, 1]
        self.assertEqual(alien_piano_mem(K, notes), 0)

    def test_02_alien_piano_mem_K8(self):
        K = 8
        notes = [2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(alien_piano_mem(K, notes), 1)

    def test_03_alien_piano_mem_K13(self):
        K = 13
        notes = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5]
        self.assertEqual(alien_piano_mem(K, notes), 0)

    def test_04_alien_piano_mem_K900(self):
        K = 900
        #Due to default value for Python max recursion depth = 10^4 we can't increase K anymore
        notes = [n for n in range(K)]
        self.assertEqual(alien_piano_mem(K, notes), 224)


class AlienPianoDPTest(TestCase):

    def test_01_alien_piano_dp_K5(self):
        K = 5
        notes = [1, 5, 100, 500, 1]
        self.assertEqual(alien_piano_dp(K, notes), 0)

    def test_02_alien_piano_dp_K8(self):
        K = 8
        notes = [2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(alien_piano_dp(K, notes), 1)

    def test_03_alien_piano_dp_K13(self):
        K = 13
        notes = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5]
        self.assertEqual(alien_piano_dp(K, notes), 0)

    def test_04_alien_piano_dp_K10000(self):
        K = 10000
        notes = [n for n in range(K)]
        self.assertEqual(alien_piano_dp(K, notes), 2499)