# Two City Scheduling - Leetcode 1029

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]  
Output: 110  
Explanation:  
The first person goes to city A for a cost of 10.  
The second person goes to city A for a cost of 30.  
The third person goes to city B for a cost of 50.  
The fourth person goes to city B for a cost of 20.  

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100  
It is guaranteed that costs.length is even.  
1 <= costs[i][0], costs[i][1] <= 1000  

## Solution

Greedy approach is about making locally optimal choices, meaning we can compare two items from the sublist and choose the smaller one, it's really simple.
However, before we do that we must have sorted costs. That's where the problem arises.

By analyzing an example we notice that more meaningful choices are those where differences between two costs are higher:
input: [[12,11], [99,10]
[99, 10] - should be considered first, this choice is more important
[12, 11] - only 1 unit difference, doesn't change much for the total
Sorting function would look like this:
```
costs.sort(key=lambda x: abs(x[0] - x[1]), reverse=True)
```
The rest of this solution is just computing the total cost for city A and B based on local choices and limit of half the people for each city.

## Data structure
Python list

## Time complexity
Time complexity is a sum of Python sort O(nlogn) and single iteration over input list O(n).  
O(nlogn + n)  
O(n(logn + 1)) - we ignore constant value  
O(nlogn)  

## Space complexity
Sorting list happens in place, no auxiliary space is required, therefore it's constant space algorithm.  
O(1)
