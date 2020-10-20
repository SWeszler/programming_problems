# Stable Wall (Google Kickstart 2020 Round C)
Apollo is playing a game involving polyominos. A polyomino is a shape made by joining together one or more squares edge to edge to form a single connected shape. The game involves combining N polyominos into a single rectangular shape without any holes. Each polyomino is labeled with a unique character from A to Z.

Apollo has finished the game and created a rectangular wall containing R rows and C columns. He took a picture and sent it to his friend Selene. Selene likes pictures of walls, but she likes them even more if they are stable walls. A wall is stable if it can be created by adding polyominos one at a time to the wall so that each polyomino is always supported. A polyomino is supported if each of its squares is either on the ground, or has another square below it.

Apollo would like to check if his wall is stable and if it is, prove that fact to Selene by telling her the order in which he added the polyominos.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the two integers R and C. Then, R lines follow, describing the wall from top to bottom. Each line contains a string of C uppercase characters from A to Z, describing that row of the wall.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a string of N uppercase characters, describing the order in which he built them. If there is more than one such order, output any of them. If the wall is not stable, output -1 instead.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ R ≤ 30.
1 ≤ C ≤ 30.
No two polyominos will be labeled with the same letter.
The input is guaranteed to be valid according to the rules described in the statement.

Test set 1
1 ≤ N ≤ 5.

Test set 2
1 ≤ N ≤ 26.

Sample

Input
 	
Output
 
4
4 6
ZOAAMM
ZOAOMM
ZOOOOM
ZZZZOM
4 4
XXOO
XFFO
XFXO
XXXO
5 3
XXX
XPX
XXX
XJX
XXX
3 10
AAABBCCDDE
AABBCCDDEE
AABBCCDDEE

  
Case #1: ZOAM
Case #2: -1
Case #3: -1
Case #4: EDCBA

  
In sample case #1, note that ZOMA is another possible answer.

In sample case #2 and sample case #3, the wall is not stable, so the answer is -1.

In sample case #4, the only possible answer is EDCBA.


## Solution
Given the picture of the wall, if two polyominos are positioned one above another, and they touch each other, then to make a stable wall, the bottom one must be placed before the top one. This gives us a set of orderings of pairs of letters which must be followed while placing the polyominos.

We can make a graph with the set of orderings just mentioned. Each polyomino/letter can be considered as a vertex, and each of the orderings can be considered as a directed edge of the graph. If the resulting graph contains any cycle, it is not possible to have a stable wall. Otherwise, we can use topological sort to find a suitable order that fulfills all the orderings. We can find all the orderings in O(R × C) time. We can find a topological sorting of the vertices of a directed acyclic graph by using depth first search. Depth first search gives us a runtime complexity of O(number of edges + number of vertices). The number of edges in the graph is at most (R-1) × C, as each cell of the grid adds at most one edge, to the cell right above it. So the total runtime complexity of this approach for each test case is O(R × C) + O(N + R × C) = O(R × C), since N can be at most R × C. This is sufficient for test set 2.

## Data structure


## Time complexity


## Space complexity
