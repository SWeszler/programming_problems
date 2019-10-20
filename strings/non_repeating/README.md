# Non-repeating character

Implement a function that takes a string and returns the first character that does not appears twice or more.
Example:
"abacc" -> "b" ("a" appears twice, and so does "c")
"xxyzx" -> "y" ("y" and "z" are non-repeating, "y" appears first)

If there's no non-repeating characters return None.

## Solution
Similarly to most frequently occurring item problem we're going to store in a hashtable a number of occurrences for each character in a string. Then in additional for loop we are looking for first one that has appeared only once.


## Data structure
Python dictionary (hashtable)


## Time complexity
Linear time
O(n)

## Space complexity
S(n) (we have to store all characters in a dictionary)