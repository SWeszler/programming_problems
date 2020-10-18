# Corporate Flight Bookings - Leetcode 1109

There are n flights, and they are labeled from 1 to n. We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5  
Output: [10,55,45,25,25]

Constraints:

1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000

Reference:  
Leetcode problem no [1109](https://leetcode.com/problems/corporate-flight-bookings/).

## Solution

Simple solution iterates over all flights in given range for each booking, its time complexity is O(n*r). That isn't efficient enough so we have to use Range Update in O(1). This approach is also known as Difference Array. In order to create Difference Array we iterate over all bookings and update first and next after last item in the range accordingly to [Difference Array | Range update query O(1)](https://www.geeksforgeeks.org/difference-array-range-update-query-o1/):

To implement Range Update like this:
update(l, r, x) : Add x to D[l] and subtract it from D[r+1], i.e., we do D[l] += x, D[r+1] -= x

We create a for loop:

```
for booking in bookings:  
    flights[booking[0] - 1] += booking[2]  
    if booking[1] < n:  
        flights[booking[1]] -= booking[2]
```

NOTICE: Indices in Python List and flight numbers aren't consistent so we subtract 1 from them, that's why result[booking[1]] doesn't have +1.

Once we get Difference Array which contains all ranges we know where each range starts and ends. Now we have to populate it across all flights. When ranges are overlapping we have to sum values up. In order to do that we need to iterate over all flights as follows:

```
s = 0
for i in range(len(flights)):
    flights[i] += s
    s = flights[i]
```

Having an array of 0s defined for all flights in the beginning that was later turned into Difference Array we could simply sum next item with previous one to populate all flight reservations. To visualize it better we create a table:

|             |     |     |     |     |     |
|-------------|:---:|:---:|:---:|:---:|:---:|
| Flights     |  1  |  2  |  3  |  4  |  5  |
| Booking #1  |  10 |     | -10 |     |     |
| Booking #2  |     |  20 |     | -20 |     |
| Booking #3  |     |  25 |     |     |     |
|             |     |     |     |     |     |
| Diff Array  |  10 |  45 | -10 | -20 |  0  |
| Sum (s)     |  0  | +10 | +55 | +45 | +25 |
| Result      |  10 |  55 |  45 |  25 |  25 |


## Data structure
Difference Array


## Time complexity
O(n+b) - where n equals number of flights and b bookings

## Space complexity
O(n)
