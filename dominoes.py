def can_chain(dominoes):
    if not dominoes:
        return []

    from collections import defaultdict

    degree = defaultdict(int)
    for a, b in dominoes:
        degree[a] += 1
        degree[b] += 1

    for v in degree.values():
        if v % 2 != 0:
            return None

    adj = defaultdict(set)
    for a, b in dominoes:
        adj[a].add(b)
        adj[b].add(a)

    if adj:
        start_node = next(iter(adj))
        visited = set()
        stack = [start_node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        if len(visited) != len(adj):
            return None

    if not degree:
        return []

    graph = defaultdict(list)
    for i, (a, b) in enumerate(dominoes):
        graph[a].append((b, i, 0))
        if a != b:
            graph[b].append((a, i, 1))

    start = next(iter(degree))
    stack = [start]
    vertex_circuit = []

    while stack:
        v = stack[-1]
        if graph[v]:
            u, idx, ori = graph[v].pop()
            if ori == 0:
                graph[u] = [(w, i, o) for w, i, o in graph[u] if not (i == idx and o == 1)]
            else:
                graph[u] = [(w, i, o) for w, i, o in graph[u] if not (i == idx and o == 0)]
            stack.append(u)
        else:
            vertex_circuit.append(stack.pop())

    vertex_circuit.reverse()

    result = []
    used = [False] * len(dominoes)

    for i in range(len(vertex_circuit) - 1):
        v, u = vertex_circuit[i], vertex_circuit[i + 1]
        found = False
        for j, (a, b) in enumerate(dominoes):
            if not used[j]:
                if a == v and b == u:
                    result.append((a, b))
                    used[j] = True
                    found = True
                    break
                elif b == v and a == u:
                    result.append((b, a))
                    used[j] = True
                    found = True
                    break
        if not found:
            return None

    return result if len(result) == len(dominoes) else None
