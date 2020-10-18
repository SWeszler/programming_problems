
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def maximum_level_sum(root):
    nodes_queue = [root]
    max_sum = float("-inf")
    max_level = 1
    level = 1

    while nodes_queue:
        size = len(nodes_queue)
        level_sum = 0

        while size > 0:
            parent = nodes_queue.pop(0)
            level_sum += parent.val

            if parent.left:
                nodes_queue.append(parent.left)
            if parent.right:
                nodes_queue.append(parent.right)

            size -= 1

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

        level += 1

    return max_level


def maximum_level_sum_queue(tree):
    from queue import Queue

    nodes_queue = Queue()
    nodes_queue.put(tree)
    max_sum = float("-inf")
    max_level = 1
    level = 1

    while not nodes_queue.empty():
        size = nodes_queue.qsize()
        level_sum = 0

        while size > 0:
            parent = nodes_queue.get()
            level_sum += parent.val
            
            if parent.left:
                nodes_queue.put(parent.left)
            if parent.right:
                nodes_queue.put(parent.right)

            size -= 1
        
        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

        level += 1

    return max_level

def maximum_level_sum_2(root):

    def pre_order(root, graph, lvl):
        if not root:
            return
        if lvl not in graph:
            graph[lvl] = 0
        
        graph[lvl] += root.val
        pre_order(root.left, graph, lvl+1)
        pre_order(root.right, graph, lvl+1)
        
    graph = {}
    
    pre_order(root, graph, 1)
    print(graph)
    ans_pair = (1,float("-inf"))
    for k,v in graph.items():
        if v>ans_pair[1]:
            ans_pair = (k,v)
    return ans_pair[0]

    


