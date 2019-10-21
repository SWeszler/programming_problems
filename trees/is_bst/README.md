# Is it a binary search tree

Write a function that takes a Binary Tree and returns True if it's a Binary Search Tree, and False if not.
Examples:  
head1 =  0  
        / \  
      1     2  
     / \   / \  
    3   4 5   6  
head1 is NOT a binary tree

head2 =  3  
        / \  
      1     4  
     / \   / \  
    0   2 5   6  
head2 is NOT a binary tree  

head3 =  3  
        / \  
      1     5  
     / \   / \  
    0   2 4   6  
head3 is a binary tree

## Solution

To find whether a given tree is Binary Search Tree or not we need a recursive function. We have to check each node if its value is between left child and right child value. Our function is using two helper variables lower_lim and upper_lim. We need this to cross check if higher child value from one subtree doesn't exceed node value from other subtree (positioned one level above). The same for lower child value from subtree.
Like in example below: 2 < 5 and 4 > 1.  
head3 =  3  
        / \  
      1     5  
     / \   / \  
    0   2 4   6  

Traversing method used here is called Preorder traversal (Root, Left, Right), it's one of Depth First Traversal methods.
To return result for left and right subtrees we have to use 'and' or '&' operator.


## Data structure
Binary tree

## Time complexity
Linear time  
O(n) - in worst case scenario we have to traverse all nodes

## Space complexity
Constant space  
O(1) - we don't need to deep copy given tree, those objects already exist in memory, however a function create_tree used for tests has linear space complexity O(n).
