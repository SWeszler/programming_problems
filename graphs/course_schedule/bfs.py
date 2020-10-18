def bfs_acyclic(node, graph):
    queue = [node]
    res = []

    while queue:
        curr = queue.pop()
        res.append(curr)

        for n in graph[curr]:
            queue.append(n)

    return res