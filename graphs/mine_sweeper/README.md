# Assign numbers in minesweeper

Implement a function that assigns correct numbers in a field of Minesweeper, which is represented as two-dimensional list.
Example: The size of the field is 3x4, and there are bombs at the position [0,0] (row index = 0, column index = 0) and [0,1] ( row index = 0, column index = 1)
Then the resulting field should be:
[[-1, -1, 1, 0],
[2, 2, 1, 0]],
[0, 0, 0, 0]]

Your function should return the resulting 2D list after taking the following three arguments:
1. bombs: A list of bomb locations. Given as a list of lists
2. num_rows: the number of rows in the resulting field
3. num_cols: the number of columns in the resulting field

Number -1 represents that there's a bomb in this location.
1,2,3,... etc. represents that there are 1,2,3,... etc. bombs in the surrounding cells (including diagonally adjacent cells).
0 represents that there are no bombs in surrounding cells.

## Solution
There's a naive solution that works well but it's not efficient. It's because it traverse each cell of the field to count surrounding bombs.
The better solution that doesn't come up to mind right away is to iterate over each of given bomb location and increment number of bombs around. The whole field is filled with "0", while traversing around bomb we just increment value in each cell.
Traversing graph requires double for loop, which gives us quadratic time. Having to check only cells around the bomb makes our algorithm much faster than checking each cell of the field. 

## Data structure
Graph (a 2D list)

## Time complexity
Linear time
O(n)
'n' represents number of bombs, so it doesn't matter that we have double for loop. It would matter if we check every single cell like it's been implemented in naive approach.

## Space complexity
Linear space
O(n)