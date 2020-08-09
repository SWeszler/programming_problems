# Alien Piano
Google Kickstart 2020 Round D
An alien has just landed on Earth, and really likes our music. Lucky for us.

The alien would like to bring home its favorite human songs, but it only has a very strange instrument to do it with: a piano with just 4 keys of different pitches.

The alien converts a song by writing it down as a series of keys on the alien piano. Obviously, this piano will not be able to convert our songs completely, as our songs tend to have many more than 4 pitches.

The alien will settle for converting our songs with the following rules instead:
The first note in our song can be converted to any key on the alien piano.
For every note after,
if its pitch is higher than the previous note, it should be converted into a higher-pitched key than the previous note's conversion;
if lower, it should be converted into a lower-pitched key than the previous note's conversion;
if exactly identical, it should be converted into the same key as the previous note's conversion.
Note: two notes with the same pitch do not need to be converted into the same key if they are not adjacent.

What the alien wants to know is: how often will it have to break its rules when converting a particular song?

To elaborate, let us describe one of our songs as having K notes. The first note we describe as "note 1", the second note "note 2", and the last note "note K."
So note 2 comes immediately after note 1.
Now if note 2 is lower than note 1 in our version of the song, yet converted to an equally-pitched or lower-pitched key (relative to note 2's conversion) in the alien's version of the song, then we consider that a single rule break.
  
Example #1:  
Input:
K = 2
notes = [1 5 100 500 1]
Output:
violations = 0

Example #2:  
Input:
K = 8
notes = [2 3 4 5 6 7 8 9]
Output:
violation = 1

We will use the notation A, B, C, D for the alien piano keys where A is the lowest note, and D is the highest. In example #1, the alien can simply map our song into the following sequence: A B C D C and this correctly reflects all the following:
our first note with pitch 1 maps to A,
our second note with pitch 5 maps to its key B. 5 > 1, and B is a higher key than A,
our third note with pitch 100 maps to its key C. 100 > 5, and C is a higher key than B,
our fourth note with pitch 500 maps to its key D. 500 > 100, and D is a higher key than C,
our fifth note with pitch 1 maps to its key C. 1 < 500, and C is a lower key than D.
So none of the rules are broken. Note: A B C D C is not the only way of conversion. A B C D A or A B C D B are also eligible conversions.

In example #2, the only conversion sequence that provides the minimal result of 1 rule broken is: A B C D A B C D. Notably, the rule break comes from the fact that our 4th note with pitch 4 is lower than our 5th note with pitch 5, but A is a lower key than D.

## Solution
Required Skills:
* replacing loops with recursion - how to convert iterative to recursive solution and vice versa  
* traversing 2 dimensional "dynamic programming" table  
* creating test cases

### Brute Force
As stated in the example #1, there can be many eligible conversions, means that we might need to test all possible conversions to find the best one (the least violations).

### Dynamic Programming - Memoization
Once we have recursive brute force solution we can implement the cache, this will increase the efficiency of our algorithm because we don't compute again occurrences with the same input values.

### Dynamic Programming - Intermediate State
In this solution we store precomputed values in the DP table, based on previous result we compute another. In the end we get our result. 

### Greedy Approach
What we should focus on here is not the combinations we have to generate but only the situation in which we break the rules. If we remove all duplicated adjacent values it's easier to count converted notes, for up and down conversion separately. We can iterate over all notes and convert them. If we reach the point when there are more than 3 (it's not 4 because we revisit previous note) conversions up or down in a row, we increase the number of violations and reset counters.  
Resetting counters is the key, for every increment of one counter we reset the other. We could have thought, instead of resetting we should be decreasing the counter because the rules say so. This isn't true tho, in this solution we find the pattern for when the violations occur. To figure out the pattern we need to take a couple of examples and do conversion manually.

## Data structure
DP - Dictionary (hashmap)  
Greedy - Python list  

## Time complexity
BF - O(4^K)  
DP - O(K) the number of Alien Piano notes is always 4, which makes it constant that we can ignore  
Greedy - O(K)  

## Space complexity
O(K)