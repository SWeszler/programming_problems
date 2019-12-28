from unittest import TestCase
from flight_bookings import flight_bookings, flight_bookings_slow

class FlightBookingsTest(TestCase):

    def test_01_flight_bookings(self):
        bookings = [[1,2,10],[2,3,20],[2,5,25]]
        n = 5
        output = [10,55,45,25,25]
        self.assertEqual(flight_bookings(bookings, n), output)


class FlightBookingsFastVsSlowTest(TestCase):

    def setUp(self):
        self.bookings = []
        self.output = []
        self.n = 20000
        for i in range(1, self.n + 1):
            self.bookings.append([1, self.n, 10000])

        for i in range(self.n):
            self.output.append(10000 * 20000)


    def test_01_flight_bookings(self):
        self.assertEqual(flight_bookings(self.bookings, self.n), self.output)


    def test_02_flight_bookings(self):
        self.assertEqual(flight_bookings_slow(self.bookings, self.n), self.output)