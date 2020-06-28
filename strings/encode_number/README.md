# Encode Number - Leetcode 1256

Given a non-negative integer num, Return its encoding string.  
The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:


0   ""  
1   "0"  
2   "1"  
3   "00"  
4   "01"  
5   "10"  
6   "11"  
7   "000"  
8   "001"  
9   "010"  


Example 1:  
Input: num = 23  
Output: "1000"  

Example 2:  
Input: num = 107  
Output: "101100"  

## Solution
How I solved this problem. After taking brute force solution with time complexity O(n) and a function to generate truth table (included in this example) I found that generating all truth tables until nth element is exponential, so in order to reverse it we can use logarithm. In most of logarithmic functions we divide our set of decoded numbers by 2 and running this function recursively.

## Data structure
Integer

## Time complexity
O(logN)

## Space complexity
O(1)