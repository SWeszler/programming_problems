# Matching Parentheses Indices

Given a string containing only parentheses, return indices of all matching parentheses.  
If some parentheses don't have a match it means that given string is invalid and you should return None.

Example:
Given input = "((())()())()", Because first pair of matching parentheses has indices [0, 9]
return [[0, 9], [1, 4], [2, 3], [5, 6], [7, 8], [10, 11]]

## Solution

The optimal solution needs a stack for finding matching pairs and a list to collect and return them in ascending order.  
Basically when we iterate over a given string we insert each character with its index to the stack.  
Whenever we've got a match with previously added character we pop those characters from a stack.  
Using removed item and current index we can create a pair of indices that we can append to the resulting list.
If our stack isn't empty after processing given string it means that some parentheses don't have a match, so this string is invalid.


## Data structure
Stack (Python list)

## Time complexity
With nested For loop:
O(N^2/4) -> O(N^2)

With dictionary (hashmap):
O(N + N/2) -> O(N)

With sorting:
O(N + N*log(N/2)/2) -> O(N)

## Space complexity
O(N)