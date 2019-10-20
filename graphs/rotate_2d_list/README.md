# Rotate 2D list by 90 degrees

Implement a function that takes a square 2D list (# columns = # rows) and rotates it by 90 degrees.
Example:
[[1,2,3],
[4,5,6],
[7,8,9]]

->

[[7,4,1],
[8,5,2],
[9,6,3]]

When you are done, try implementing this function so that you can solve this problem in place. Solving it in place means that your function won't create extra list of lists. Instead, modify the content of the given list with O(1) extra space.

## Solution

This problem can be solved out-of-place or in-place, which means we don't need to create a copy of given list.
For simplicity we begin with out-of-place solution.
First and foremost we must make a deep copy of given list.
After that, we use a double for loop to assign each element from given list to the rotated resulting list. It's made by the following rule:
new_i = j (swapping i with j)
new_j = n - 1 - i (going backwards)


## Data structure
Two-dimensional Python list

## Time complexity
O(n^2) - considering 'n' as one of the sides of squared 2D list

## Space complexity
O(n^2) - considering 'n' as one of the sides of squared 2D list