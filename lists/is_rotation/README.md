# Is list a rotation of another list

Write function that returns True if a list is rotation of another list.
Example: list [1,2,3,4,5,6,7] is a rotation of [4,5,6,7,1,2,3]
NOTE: There are no duplicates in each of these lists.

# Solution
First we are trying to find index (position) of element that occurs as first one in given list1. If this element doesn't exist or lists have different lengths we can immediately return False.
If element is found and we have it's index we can use this as an offset for list2. While iterating both lists in one loop we return False if elements aren't equal. Otherwise function returns True, which means all elements have been found and have the same order in both lists.


## Data structure:
Integer value.

## Time complexity:
Linear time (iterate over each element from input list)
O(n)

## Space complexity:
Constant space
S(1)