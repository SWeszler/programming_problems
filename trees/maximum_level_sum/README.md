# Maximum Level Sum of Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.  
Return the smallest level X such that the sum of all the values of nodes at level X is maximal.  

Input: [1,7,0,7,-8,null,null]  
Output: 2  
Explanation:   
Level 1 sum = 1.  
Level 2 sum = 7 + 0 = 7.  
Level 3 sum = 7 + -8 = -1.  
So we return the level with the maximum sum which is level 2.  

Note:  

The number of nodes in the given tree is between 1 and 10^4.  
-10^5 <= node.val <= 10^5  

## Solution
To solve this problem we must traverse each level of the tree, sum up all nodes and find the highest sum.
Level order traversal requires a loop and queue, but this isn't enough to find level sum.
The maximum size of queue represents number of nodes on each level, so we use this fact while adding up node values.  

It's very important to use the smallest negative value for max_sum, because node values are between -10^5 and 10^5.
In python we use float("-inf"), it gives us the smallest negative floating point number.

## Data structure
Queue (Python list)

## Time complexity
O(n) - to count sum of all levels we need to traverse whole tree

## Space complexity
O(n) - in the worst case we need to store all nodes in the queue
