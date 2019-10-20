# One way string

Write a function that takes two strings and returns True if they are one way from each other.
They are one way from each other if a single operation (changing, deleting or adding a character) will change one of the string to the other.
Examples:
"abcde" and "abcd" are one way (deleting/adding a character)
"a" and "a" are one way (changing the only character "a" to the equivalent character "a")
"abc" and "bcc" are NOT one way (they are two operations away)

## Solution
This problem is a little bit more complicated and needs to broken down. There are 3 cases we have to consider. First one is when the length difference between two strings is greater than 1, it immediately means that we can return False, because they can't be one way strings.
Second case is when lengths are the same, and third one is when length difference equals one.
When we get the same lengths we can simply iterate over a string and compare equivalent characters. If more than one pair or characters is different to each other we return False, otherwise return True.

The most difficult case is when we've got different lengths strings.
Same as before we define count_diff, which will count operations, and for loop to iterate over a string.
This variable can be used as an offset for second string while comparing characters. Whenever characters are different we increment count_diff, this way we can track how many changes need to be made and we move our pointer at the same time.
TIP: In order not to exceed list index we use modulo operator and list length.

## Data structure
Single integer to count changes

## Time complexity
Linear time
O(n)

## Space complexity
Constant space
S(1)
