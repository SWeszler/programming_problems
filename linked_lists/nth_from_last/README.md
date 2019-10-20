# N-th element of a linked list

Implement a function that finds and returns n-th node in a given linked list, counting from the end.
Your function should take linked list (its head element) and n, a positive integer as its arguments.
Example:
head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> None
The third element of head counting from the end is 3.

head2 = 1 -> 2 -> 3 -> 4 -> None
The fourth element of head counting from the end is 1.

If the given n is larger than the number of nodes in the list, return None.

## Solution

Naive solution requires to store each element of the list, which makes it not acceptable.
The better solution is to traverse this list using two nodes, one node called 'end' is ahead of 'n' children from 'start'. When 'end' node hits the end of the list (None) 'start' node is on the position we need to return from our function.

## Data structure
One-directional linked list

## Time complexity
Linear time
O(n) - we have to traverse all elements in the list

## Space complexity
Constant space
O(1) - there are only two objects we need to store in memory
