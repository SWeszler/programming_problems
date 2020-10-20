def stable_wall(R, C, rows):
    res = []
    graph = {}
    in_degree = {}
    res = ''

    for i in range(R):
        for j in range(C):
            if rows[i][j] not in graph:
                graph[rows[i][j]] = set()
            if rows[i][j] not in in_degree:
                in_degree[rows[i][j]] = 0

    for c in range(C):
        for r in range(R - 1, 0, -1):
            if rows[r][c] != rows[r - 1][c]:
                graph[rows[r][c]].add(rows[r - 1][c])

    for k, v in graph.items():
        for n in v:
            in_degree[n] += 1

    queue = [k for k, v in in_degree.items() if v == 0]

    while queue:
        curr = queue.pop()
        res += curr

        for n in graph[curr]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)

    return res if len(res) == len(graph) else -1