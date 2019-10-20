# Most frequently occurring item in a list

Find the most frequently occurring item in a list.
Example: the most frequently occurring item in list [1,2,3,1,3,1] is 1

If you are given empty list you should return None.

You can assume that there's always a single unique value that appears most frequently unless list is empty. For instance, you won't be given an list such ass [1,1,2,2].

## Solution

Naive approach would use double for loop, but this isn't acceptable. We have to store all occurrences in a dictionary and increment their numbers whenever it appears again, as a result we get item which has the highest number.

## Data structure
Python dictionary (hashtable)

## Time complexity
Linear time
O(n)

## Space complexity
Linear space
O(n)