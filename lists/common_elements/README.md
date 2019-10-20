# Common elements in two sorted lists

Write a function that returns the common elements (as a list) between two sorted lists or integers (ascending order).

Example: The common elements between [1,3,4,6,7,9] and [1,2,4,5,9,10] are [1,4,9]

## Solution
To solve this problem we need to iterate over one list and check if current element exists in second given list.

NAIVE solution.
For iteration I'm going to use "for" loop and for checking if item exists in the list "in" operator. This gives us readable code but not good performance.
"in" operator has linear time complexity, used in for loop gives us quadratic time.

Optimal solution.
In order to achieve linear time we must use two pointers and one loop. Thanks to sorted input we can increment pointers accordingly to the result of comparison two values, if both values are equal we increment both pointers, if one value is higher than another we increment only pointer of a list with lower current value.

## Data structure:
Resizable Python list.

## Time complexity:
Linear time
O(n)

## Space complexity:
Constant space
O(1)