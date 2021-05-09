# Minimum Cost For Tickets - Leetcode 983
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

**Example 1:**

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.

**Example 2:**

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
 

Note:

1 <= days.length <= 365  
1 <= days[i] <= 365  
days is in strictly increasing order.  
costs.length == 3   
1 <= costs[i] <= 1000  
 
## Solution
**Problem Type: Optimization Problem (tractable)**  
Required skills:
- find max or min from array recursively
- find sum of array recursively
- cache function result (memoization)
- dynamic programming tabulation
- visualize the problem as a table
- size the table based on the inputs (tractable solution)

## Dynamic Programming - Memoization
First approach is brute-force. We try to compute all possible combinations of passes purchased to travel in all days. This can be visualized in a tree, each node represents a day in which we must buy a new pass, (cost) - represents cost of a particular pass.

```
              start  
           ____________
         /      \       \ 
       /          \       \  
     1(2)         1(7)     1(15)  
   /  |  \        /  |  \      \  
4(2) 4(7) 4(30)  7(2)7(7)7(30)  20(0)
```
In order to find the smallest total cost for each branch we must traverse this tree. Every time we move to another day we have 3 options to choose. This makes the time complexity exponential, in a worst case it's O(N^3).
To optimize it we can use memoization (caching). Cost for some od the days has already been computed, we don't have to do that again, the result can be stored and reused.


## Data structure
**Python List**

## Time complexity
O(3^N) - brute force
O(N*M) - dynamic programming memoization (recursive)
O(N^2) - dynamic programming tabulation (bottom up, intermediate state, iterative)

## Space complexity
O(1) - brute force
O(3^N) - dynamic programming memoization (recursive)
O(N*M) - dynamic programming tabulation (bottom up, intermediate state, iterative)