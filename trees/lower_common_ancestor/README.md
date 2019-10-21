# Lowest common ancestor in a binary tree

Find the lowest common ancestor of two items in a binary tree.

Assumptions:
- each value in the tree is unique (there are no two nodes with the same value)
- each node has at most two children (left and right)
- you don not have level attribute in each of your nodes (for instance 1st layer, 2nd layer and so on)
- each node has pointers to left and right children, but there's no back link (a child does not point back to its parent node)

Example:  
   head = 5  
        /  \  
      1      4  
     /  \   /  \  
    3   8   9   2  
   / \  
  6   7  

LCA of 8 and 7 is 1
LCA of 4 and 2 is 4

## Solution

To solve this problem first we must create a function that will return a path from the root to the node we are looking for. We can return it as a stack or list. The crucial here is that first element added to the stack/list will be the element we're looking for:
if root.value == x:
    return [root]
Having two stacks with all nodes representing paths we use while loop to scan through them and find lowest common ancestor. While loop works until paths have the same nodes, if a pair of nodes have different values we break the loop.

## Data structure
Stack represented as python list.

## Time complexity
O(n)

## Space complexity
O(logN) - for balanced tree. LogN is basically a hight of the tree, which is also the longest path.
