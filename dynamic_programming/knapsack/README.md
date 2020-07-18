# 0-1 Knapsack problem
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays value[0..n-1] and weight[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don't pick it (0-1 property).

Example:
value = [60, 100, 120]  
weight = [10, 20, 30]  
W = 50
Answer: 220

## Solution
How to build two-dimensional DP table:
1) It's easier to determine the value we need to store than the dimensions of a table. In this case we need to compute and store the max sum of items from the value array. This means the max value can't be one of the two dimensions.
2) The remaining inputs we've got are weights and knapsack capacity - W. Both are represented by integer numbers, so we can easily distribute them on a DP table.


## Data structure
Two dimensional list of integers

## Time complexity
O(n*W) - n is the number of all values (the same as weights) and W is a capacity of the knapsack

## Space complexity
O(n*W) - this is exactly the size of two dimensional DP table