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
Required Skills:
* replacing loops with recursion - how to convert iterative to recursive solution and vice versa  
* combinatorics - permutations with repetition  

### Brute Force
For better understanding of the problem we're going to start with brute force solution.
To create all possible combinations of plates that Dr. Patel could pick, we can use "product" function from Python itertools library.

Very important to note is that we don't create combinations from a set of plates, we can only pick a plate from the top of a stack so we must create combinations of numbers of plates to pick from each stack. According to Example #1, we could pick the following numbers of plates from each stack respectively:  
[1, 4]  
[2, 3]  
[3, 2]  
[4, 1]  

How to generate these combinations programmatically? We need nested for-loops for that.
(FYI: In combinatorics we would rather use term permutations with repetition instead of combinations)

2 stacks of plates with 4 plates in each stack, we include 0 because there might be a case in which we don't pick any plate from one stack  
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

From a 2 sets of 5 items we get 25 permutations, the time complexity for product is O((K+1)^N). In this case we can ignore the constant value, so we get O(K^N). The total time complexity is even higher because we need to calculate sums.
This obviously isn't an optimal solution, in the next step we'll use dynamic programming to optimize it.
There are two distinct approaches to Dynamic Programming, one is Memoization and the other is Intermediate State, also called Bottom-Up approach, we'll go through both of them.  
To begin with Memoization we need to replace intertool.product with our own recursive implementation. We'll call it combinations because we don't need all permutations with repetition.  
We can get our algorithm working by implementing helper recursive function called combinations and iterate over the result to calculate sums and find max.  
This will work but it still isn't optimal. In the next step we combine generating combinations and finding max value in one recursive function findMax. This is the most efficient brute force approach.  
Note that, we replace Python built-in function sum() with += operator:  
```
for i, np in enumerate(p):
    s += sum(stacks[i][:np])
```
```
s = 0
for y in range(min(plates_to_pick, K)):
    s += stacks[n_stacks][y]
```
This makes a huge difference when we have large number of plates in the stack. Running sum() for number of items in the stack takes O(n), this is very inefficient. We can compute subsequent sums by incrementing previously computed sum, which will only take one operation - O(1).  


### Memoization
Now, when we have recursive function which takes only two arguments that change during the computation, we can implement Memoization/cache. Let's take an advantage of Python defaultdict, it's a very convenient way of construction an empty dictionary to store precomputed max values for each stack and number of plates to pick.
```
dp = defaultdict(lambda: defaultdict(int))
```
The idea of caching is very simple, we store all computed values in our dp dictionary and retrieve it for existing keys n_stack and plates_to_pick. This is to eliminate all recursive calls that have already been computed.

### Intermediate State
As an alternative to Memoization we'll now use Intermediate State dp table. The concept is pretty much the same, we also create a dictionary dp with two dimensions, N - number of stacks and P - plates to pick, but instead of recursion we write nested for-loops. This requires to precompute sum of the first x plates for each stack. Once we're done with it we can start populating max values found so far for each of the dp table cell, starting from top left corner. The essential part of the entire algorithm is this formula:
```
dp[i][j] = max(dp[i][j], sums[i][x] + dp[i - 1][j - x])
```
that if we look closer resembles this operation from our recursive solution:
```
max_val = max(max_val, s + findMax(n_stacks - 1, plates_to_pick - y - 1))
```
## Data structure
Dictionary (hashmap)

## Time complexity
Dynamic Programming - O(N*P*K)
Brute Force - O(K^N)

## Space complexity
O(N*P)