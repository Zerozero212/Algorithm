from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    dist = [-1] * (n + 1)  # -1이면 아직 방문하지 않음
    dist[1] = 0            # 1번 노드 시작점

    q = deque([1])
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if dist[nxt] == -1:         # 아직 방문 안 했으면
                dist[nxt] = dist[node] + 1
                q.append(nxt)

    max_dist = max(dist)
    return dist.count(max_dist)
