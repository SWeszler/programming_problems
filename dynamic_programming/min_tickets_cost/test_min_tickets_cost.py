from unittest import TestCase
from min_tickets_cost import min_tickets_cost_mem, min_tickets_cost_bf, min_tickets_cost_tab


class MinTicketsCostBFTest(TestCase):

    def setUp(self):
        self.days = [1, 4, 6, 7, 8, 20]
        self.costs = [2, 7, 15]

    def test_01_min_tickets_cost(self):
        self.assertEqual(min_tickets_cost_bf(self.days, self.costs), 11)

    def test_02_min_tickets_cost(self):
        self.days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
        self.assertEqual(min_tickets_cost_bf(self.days, self.costs), 17)

    def test_03_min_tickets_cost(self):
        self.days = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                     10, 30, 31, 100, 101, 102, 103, 104]
        self.assertEqual(min_tickets_cost_bf(self.days, self.costs), 24)


class MinTicketsCostMemTest(TestCase):

    def setUp(self):
        self.days = [1, 4, 6, 7, 8, 20]
        self.costs = [2, 7, 15]

    def test_01_min_tickets_cost(self):
        self.assertEqual(min_tickets_cost_mem(self.days, self.costs), 11)

    def test_02_min_tickets_cost(self):
        self.days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
        self.assertEqual(min_tickets_cost_mem(self.days, self.costs), 17)

    def test_03_min_tickets_cost(self):
        self.days = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                     10, 30, 31, 100, 101, 102, 103, 104]
        self.assertEqual(min_tickets_cost_mem(self.days, self.costs), 24)


class MinTicketsCostTabulationTest(TestCase):

    def setUp(self):
        self.days = [1, 4, 6, 7, 8, 20]
        self.costs = [2, 7, 15]

    def test_01_min_tickets_cost(self):
        self.assertEqual(min_tickets_cost_tab(self.days, self.costs), 11)

    def test_02_min_tickets_cost(self):
        self.days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
        self.assertEqual(min_tickets_cost_tab(self.days, self.costs), 17)

    def test_03_min_tickets_cost(self):
        self.days = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                     10, 30, 31, 100, 101, 102, 103, 104]
        self.assertEqual(min_tickets_cost_tab(self.days, self.costs), 24)
