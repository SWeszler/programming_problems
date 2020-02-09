# Leetcode - 1300. Sum of Mutated Array Closest to Target

Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not necessarily a number from arr.


Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5

## Solution
First and foremost we try to break this down.
We have to test multiple values to find the best one.
To solve this problem with optimal time complexity we're going to use binary search algorithm.
1. Create a function that will replace and sum all items in given list
2. Assign left and right values for binary search, minimum and maximum possible. Note that those values are not necessarily in given list.
3. Using binary search find two closest values
4. Choose from two values which one is closer to given target

For binary search, it explains how to find middle value:
mid = l + (r - l)/2
mid = l + r/2 - l/2
mid = 2l/2 + r/2 - l/2
mid = l/2 + r/2
mid = (l + r)/2

## Data structure


## Time complexity


## Space complexity
