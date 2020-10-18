# Programming Problems Collection
by Sebastian Weszler

## Lists
1. Most frequently occurring item in the list.
2. Common elements in two sorted lists.
3. Is list a rotation of another list.
4. Corporate Flight Bookings - Leetcode 1109 [difference_array]
5. Find best value. Sum of Mutated Array Closest to Target. [binary_search]
6. K Closest Points to origin [quicksort]
7. Rotate 2D list by 90 degrees

## Strings
1. Non-repeating character.
2. One way string.
3. Compare strings by which one is strictly smaller
4. Matching Parentheses
5. Count and Say
6. Encode Number - Leetcode 1256

## Graphs
1. Assign numbers in Minesweeper
2. Find where to expand in Minesweeper
3. Course Schedule - Leetcode 207 [dfs, bfs, kahns_top_sort] - WIP
4. Stable Wall (Google Kickstart 2020 Round C) - WIP

## Linked Lists
1. N-th element of a linked list
2. Delayed Projects - WIP

## Trees
1. Is it a binary search tree
2. Lowest common ancestor of two items in binary tree
3. Maximum level sum

## Dynamic Programming
1. Knapsack problem  
2. Plates (Google KickStart 2020 Round A)  

## Greedy
1. Alien Piano (Google KickStart 2020 Round D)
2. Two City Scheduling - Leetcode 1029

## Techniques
1. Analyse solution on paper.
2. Big picture first, then details. If this is large problem, break it down into smaller functions (representing steps or different cases), keep your algorithm loosely coupled with the data structure. Use known data structure.
3. B.U.D.  
Bottleneck - Identify a bottleneck and get rid of it. An example problem could be two lists that we must iterate to find a common items.
Instead of iterating both lists we can store one of them in a data structure that allows us quick (constant) look-up.  
Unnecessary work - Try a brute force solution and look for unnecessary work that can be eliminated.   
Duplicated work - The same as for unnecessary work, try to eliminate operations that are duplicated in your brute force solution.
4. Space/Time tradeoff. Most of the time when you want to improve your algorithm and make it working faster it must use more space, which means you must store more data in memory. This should lead you to choosing proper data structure that eventually helps you solve this problem optimally.
5. D.I.Y (do it yourself) Use big example and try to solve it manually, you might be able to reverse engineer your thought process (your brain algorithm)
6. Communicate your thoughts, speak about it. Make sure all your assumptions are correct.
7. While working with more complicated recursive functions use The Call Stack to visualize execution for each function call.
8. It might not be applicable to many problems, but whenever the optimization of the algorithm is needed it's worth to consider next known better time complexity [Big O Cheat Sheet](https://www.bigocheatsheet.com/). For instance if O(n) isn't enough try O(logN), which can be achieved by dividing your set of data by 2 and run your function recursively until finding a result. (Divide and conquer)
9. From a brute force solution find a pattern or sequence, if this is arithmetic or geometric sequence you can apply mathematical equation to find sum of a sequence or nth element.
10. To find patterns, consider all test cases and analyse them one by one, use bigger sets of input data.


## Testing

```
pytest ./
```