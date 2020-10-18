def dfs_acyclic(node, graph):
    res = []
    def helper(node, visited):
        visited.append(node)
        for n in graph[node]:
            helper(n, visited)

    helper(node, res)
    return res