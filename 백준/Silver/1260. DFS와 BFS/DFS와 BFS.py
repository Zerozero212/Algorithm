from collections import deque
import sys
input=sys.stdin.readline

def dfs(dfs_node):
    if dfs_visited[dfs_node]: return
    else:
        dfs_visited[dfs_node] = 1
        dfs_answer.append(dfs_node)
        for linked_node in arr[dfs_node]:
            dfs(linked_node)

def bfs(bfs_node):
    q=deque([bfs_node])
    bfs_visited[bfs_node]=1
    while q:
        new_node = q.popleft()
        bfs_answer.append(new_node)
        for linked_node in arr[new_node]:
            if not bfs_visited[linked_node]: 
                bfs_visited[linked_node]=1
                q.append(linked_node)

# 입력
N,M,V = map(int,input().split())
arr = [[] for _ in range(N+1)]

# 인접 리스트 생성
for _ in range(M):
    node1,node2 = map(int,input().split())
    arr[node1].append(node2)
    arr[node2].append(node1)
arr = [sorted(x) for x in arr]

# dfs 준비
dfs_visited = [0]*(N+1)
dfs_answer = []
dfs(V)

# bfs 준비
bfs_visited = [0]*(N+1)
bfs_answer = []
bfs(V)

print(*dfs_answer)
print(*bfs_answer)