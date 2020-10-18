def kahns_top_sort(graph):
    """Kahn's topological sort"""
    in_degree = [0] * len(graph)
    queue = []
    res = []

    for k, v in graph.items():
        for n in v:
            in_degree[n] += 1

    for i, n in enumerate(in_degree):
        if n == 0:
            queue.append(i)

    while queue:
        curr = queue.pop()
        res.append(curr)

        for n in graph[curr]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)

    return res



