# Programming Problems Collection
by Sebastian Weszler

## Lists
1. Most frequently occurring item in the list.
2. Common elements in two sorted lists.
3. Is list a rotation of another list.


## Strings
1. Non-repeating character.
2. One way string.
3. Compare strings by which one is strictly smaller

## Graphs (two-dimensional lists)
1. Assign numbers in Minesweeper
2. Find where to expand in Minesweeper
3. Rotate 2D list by 90 degrees

## Linked Lists
1. N-th element of a linked list


## Trees
1. Is it a binary search tree
2. Lowest common ancestor of two items in binary tree


## Techniques
1. Analyse solution on paper.
2. Big picture first, then details. If this is large problem break down into smaller functions (representing steps or different cases), separate algorithm from data structure. Use known data structure.
3. B.U.D.  
Bottleneck - Identify a bottleneck and get rid of it. An example problem could be two lists that we must iterate to find a common items.
Instead of iterating both lists we can store one of them in a data structure that allows us quick (constant) look-up.  
Unnecessary work - Try a brute force solution and look for unnecessary work that can be eliminated.   
Duplicated work - The same as for unnecessary work, try to eliminate operations that are duplicated in your brute force solution.
4. Space/Time tradeoff. Most of the time when you want to improve your algorithm and make it working faster it must use more space, which means you must store more data in memory. This should lead you to choosing proper data structure that eventually helps you solve this problem optimally.
5. D.I.Y (do it yourself) Use big example and try to solve it manually, you might be able to reverse engineer your thought process (your brain algorithm)
6. Communicate your thoughts, speak about it. Make sure all your assumptions are correct.

## Testing

```
pytest ./
```