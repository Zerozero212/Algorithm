import sys
input = sys.stdin.readline
V, E, R = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort()

visited = [0] * (V + 1)
stack = [R]
order = 1
while stack:
    node = stack.pop()
    if visited[node]:
        continue
    visited[node] = order
    order += 1
    for nxt in reversed(graph[node]):
        if not visited[nxt]:
            stack.append(nxt)

print('\n'.join(map(str, visited[1:])))
