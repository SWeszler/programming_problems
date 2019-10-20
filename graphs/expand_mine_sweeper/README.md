# Find where to expand in Minesweeper

Implement a function that turns revealed cells into -2 given a location the user wants to click.

For simplicity only reveal cells that have 0 in them. If the user click on any other type of cells (for example -1 / bomb, or 1,2 or 3) just ignore the click and return original field. If a user click 0, reveal all other 0's that are connected to it.
Example 1:
Given field:

## Solution
To solve this problem we have to start with checking if clicked cell equals 0. If not we have to return a field as is, otherwise we store first cell location in a queue and replace its value in a field with -2. Next we must check all connected cells with value 0 and add them to the queue for further check.
In a 'while' loop we run our check until queue is empty.
For checking surrounding cells we use double 'for' loop with a range plus and minus one from current location.

## Data structure
Python queue (we could use Python list in a similar manner, but pop method has much lower efficiency so we decide to use Queue)

## Time complexity
Considering 'n' as number of cells with value 0 time complexity is linear.
O(n)

## Space complexity
Constant space 
O(1) - in the worst case scenario the queue will have 8 surrounding elements, it's because each examined cell is removed from the queue and its value is replaced with -2
