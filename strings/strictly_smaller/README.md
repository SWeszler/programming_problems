# Compare strictly smaller strings

One string is strictly smaller than another when the frequency of occurrence of the smallest character in the string is less than the frequency of occurrence of the smallest character in the comparison string.

For example, string "abcd" is smaller than string "aaa" because the smallest character (in lexicographical order) in "abcd" is 'a', with a frequency of 1, and the smallest character in "aaa" is also 'a', but with a frequency of 3. In another example, string "a" is smaller than string "bb" because the smallest character in "a" is 'a' with frequency of 1, and the smallest character in "bb" is 'b' with a frequency of 2.

Writhe a function that given string A (which contains M strings delimited by ',') and string B (which contains N strings delimited by ','), returns an array C of N integers. For 0 <= J < N, values of C[J] specify the number of strings in A which are strictly smaller than the comparison J-th string in B (starting from 0).

For example, given strings A and B such that:
A = "abcd,aabc,bd"
B = "aaa,aa" 
the function should return [3,2], because:
All the strings in the array are strictly smaller than "aaa" on the basis of the given comparison criteria; Strings "abcd" and "bd" are strictly smaller than "aa".

Assume that:
- 1 <= N, M <= 10000
- 1 <= length of any string contained by A or B <= 10
- All the strings comprise only lowercase English alphabet letters (a-z)


In your solution, focus on correctness. The performance of your solution will not be the primary focus of the assessment.

## Solution
First of all we need to split given strings by ',' to find frequency of smallest character. In order to achieve linear time we need to group strings from a list A. We are grouping them by frequency, this will help us find sum of all strings with frequency lower than a particular string from list B. 

## Data structure
Python Dictionary

## Time complexity
O(n+m)

## Space complexity
O(1)