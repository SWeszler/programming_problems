from unittest import TestCase
from maximum_level_sum import maximum_level_sum, TreeNode
from queue import Queue

def create_binary_tree(items):

    child_index = 1
    root = TreeNode(items[0])
    nodes_queue = Queue()
    nodes_queue.put(root)
    
    while child_index < len(items):
        parent = nodes_queue.get()
        
        item = items[child_index]
        child_index += 1

        if item != 'null':
            parent.left = TreeNode(item)
            nodes_queue.put(parent.left)

        if child_index >= len(items):
            break

        item = items[child_index]
        child_index += 1
        if item != 'null':
            parent.right = TreeNode(item)
            nodes_queue.put(parent.right)

    return root

def print_preorder(tree):
    if tree:
        print(tree.val)
        print_preorder(tree.left)
        print_preorder(tree.right)



class MaximumLevelSumOfBinaryTreeTest(TestCase):

    def test_01_maximum_level_sum(self):
        tree_list = [1,7,0,7,-8,'null','null']
        tree = create_binary_tree(tree_list)

        self.assertEqual(maximum_level_sum(tree), 2)

    def test_02_maximum_level_sum(self):
        tree_list = [39608,'null',-34332,84856,62101,98129,'null','null',-26118,'null',57785,-75141,'null','null',-63491,-63367]
        tree = create_binary_tree(tree_list)

        self.assertEqual(maximum_level_sum(tree), 3)

    def test_03_maximum_level_sum(self):
        tree_list = [989,'null',10250,98693,-89388,'null','null','null',-32127]
        tree = create_binary_tree(tree_list)

        self.assertEqual(maximum_level_sum(tree), 2)