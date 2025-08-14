from collections import defaultdict, deque

N, M = map(int, input().split())
seqs = [tuple(map(int, input().split())) for _ in range(N - M + 1)]

# 그래프 생성: 앞 (M-1) → 뒤 (M-1)
graph = defaultdict(deque)
indegree = defaultdict(int)
outdegree = defaultdict(int)

for s in seqs:
    prefix = s[:-1]  # 앞 M-1개
    suffix = s[1:]   # 뒤 M-1개
    graph[prefix].append(suffix)
    outdegree[prefix] += 1
    indegree[suffix] += 1

# 시작 노드 찾기
start = None
for node in graph:
    if outdegree[node] - indegree[node] == 1:
        start = node
        break
if start is None:
    start = seqs[0][:-1]

# 오일러 경로 (Hierholzer 알고리즘)
path = []
stack = [start]
while stack:
    cur = stack[-1]
    if graph[cur]:
        nxt = graph[cur].popleft()
        stack.append(nxt)
    else:
        path.append(stack.pop())

path.reverse()

# 수열 복원
result = list(path[0])
for p in path[1:]:
    result.append(p[-1])

print(*result)
