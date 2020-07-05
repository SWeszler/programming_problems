# Plates
Google Kickstart 2020 Round A
Dr. Patel has N stacks of plates. Each stack contains K plates. Each plate has a positive beauty value, describing how beautiful it looks.

Dr. Patel would like to take exactly P plates to use for dinner tonight. If he would like to take a plate in a stack, he must also take all of the plates above it in that stack as well.

Help Dr. Patel pick the P plates that would maximize the total sum of beauty values. The beauty values are between 1 and 100, inclusive.

Example #1:
Input:
stacks - N = 2
plates in stack - K = 4 
plates to pick - P = 5
values:
10 10 100 30
80 50 10 50
Output:
max_beauty = 250

Example #2:
Input:
stacks - N = 3
plates in stack - K = 2
plates to pick - P = 3
values:
80 80
15 50
20 10
Output:
max_beauty = 180

In Example #1, Dr. Patel needs to pick P = 5 plates:
He can pick the top 3 plates from the first stack (10 + 10 + 100 = 120).
He can pick the top 2 plates from the second stack (80 + 50 = 130) .
In total, the sum of beauty values is 250.

In Example #2, Dr. Patel needs to pick P = 3 plates:
He can pick the top 2 plates from the first stack (80 + 80 = 160).
He can pick no plates from the second stack.
He can pick the top plate from the third stack (20).
In total, the sum of beauty values is 180.

## Solution
For better understanding of a problem like this we're going to start with brute force solution.
To create all possible combinations of plates that Dr. Patel could pick, we can use "product" function from Python itertools library.

Very important to note is that we don't create combinations from a set of plates, we can only pick a plate from the top of a stack so we must create combinations of numbers of plates to pick from each stack. According to Example #1, we could pick the following numbers of plates from each stack respectively:  
[1, 4]  
[2, 3]  
[3, 2]  
[4, 1]  

How to generate these combinations programmatically? We need nested for-loops for that.
(FYI: In combinatorics we would rather use term permutations with repetition instead of combinations)

2 stacks of plates with 4 plates in each stack, we include 0 because it might happen when we don't pick any plate from one stack  
{0, 1, 2, 3, 4} x {0, 1, 2, 3, 4}  
itertools.product (Cartesian product of input iterables) is roughly an equivalent of nested for-loops, to find Python implementation go to https://docs.python.org/3/library/itertools.html#itertools.product

From itertools.product we get all possible permutations with repetition:  
~~(0, 0)~~  
~~(0, 1)~~  
~~(0, 2)~~  
~~(0, 3)~~  
~~(0, 4)~~  
~~(1, 0)~~  
~~(1, 1)~~  
~~(1, 2)~~  
~~(1, 3)~~  
(1, 4)  
~~(2, 0)~~  
~~(2, 1)~~  
~~(2, 2)~~  
(2, 3)  
~~(2, 4)~~  
~~(3, 0)~~  
~~(3, 1)~~  
(3, 2)  
~~(3, 3)~~  
~~(4, 0)~~  
(4, 1)  
~~(4, 2)~~  
~~(4, 3)~~  
~~(4, 4)~~  

From a 2 sets of 5 items we get 25 permutations, the time complexity for product is O((K+1)^N), in this case we can ignore the constant value, so we get O(K^N). The total time complexity is even higher because we need to calculate sums.
This obviously isn't an optimal solution, in the next step we'll use dynamic programming to optimize it.
There are two distinctly different approaches to Dynamic Programming, one is Memoization and the other is Intermediate State, also called Bottom-Up, we'll go through both of them.  
To begin with Memoization we need to replace intertool.product with our own recursive implementation. We'll call it combinations because we don't need all permutations with repetition.

## Data structure


## Time complexity


## Space complexity
