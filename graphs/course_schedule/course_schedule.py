def course_schedule_dfs(N, prerequisites):
    from collections import defaultdict
    graph = defaultdict(list)
    
    for c1, c2 in prerequisites:
        graph[c1].append(c2)
        
    def has_cycle(node, visited):
        if node in visited:
            return True
        
        visited.add(node)
        for n in graph[node]:
            if has_cycle(n, visited):
                return True
            
        visited.remove(node)
            
    for c in range(N):
        if has_cycle(c, set()):
            return False
    
    return True


def course_schedule_bfs(N, prerequisites):
    from collections import defaultdict
    graph = defaultdict(list)
    in_degree = [0] * N
    queue = []
    count = 0

    for c1, c2 in prerequisites:
        graph[c1].append(c2)

    for i in range(N):
        for j in graph[i]:
            in_degree[j] += 1

    for i, n in enumerate(in_degree):
        if n == 0:
            queue.append(i)

    while queue:
        curr = queue.pop()

        for n in graph[curr]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)

        count += 1

    return N == count


course_schedule = course_schedule_bfs