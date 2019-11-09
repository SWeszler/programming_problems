# Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1  
2.     11  
3.     21  
4.     1211  
5.     111221  
1 is read off as "one 1" or 11.  
11 is read off as "two 1s" or 21.  
21 is read off as "one 2, then one 1" or 1211.  

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.  
Note: Each term of the sequence of integers will be represented as a string.  

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

## Solution
To solve this problem we have to define first term as "1" and start generating next elements until we get nth one.  
For each terms we need to count all the same adjacent digits and return new formatted string, which will be used in another iteration as input. 
The most tricky part here is counting numbers in a string. In some naive solution we might think of using index minus one for previous element. However this isn't a good approach, it's better to keep previous element in additional variable, for example 'prev', and assign to it each character in the end of counting loop.  
While comparing previous and current element we increment 'count' variable or append it to resulting string and reset to 1. (IT MUST NOT BE 0, BECAUSE NEW CURRENT ELEMENT IS ALREADY COUNTED).
By using 'prev' instead of current index minus one (j - 1) we don't have to worry about having negative index, so this definitely won't cause any issues.  
The last problem with counting adjacent digits is when we've got the last character in a string. Ending a loop with condition that only increments 'count' and doesn't append it to resulting string isn't desired. We must append it outside counting loop, the value of 'count' and 'prev' is still in memory so we can easily call it and append to new resulting string.  
If our main loop needs to proceed to another term we use this new resulting string as an input for another iteration.

## Data structure
String

## Time complexity
O(n * k) - where k could be an average length of a term

## Space complexity
O(k) - k is an average length of a term we need to store for each iteration
