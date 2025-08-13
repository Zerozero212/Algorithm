from collections import deque
def is_zero():
    for i in range(N):
        for j in range(M):
            if not arr[i][j]: return 1
    return 0

dir1 = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(one_arr):
    q = deque([*one_arr])
    if not q: return 0
    while q:
        i,j = q.popleft()
        for di,dj in dir1:
            ni,nj = i+di,j+dj
            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
                arr[ni][nj] = arr[i][j] + 1
                q.append((ni,nj))
    return arr[i][j]-1

M,N = map(int,input().split())
arr = []
one_idx = []
for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(M):
        if temp[j] == 1: one_idx.append((i,j))
    arr.append(temp)

answer = bfs(one_idx)
result = -1 if is_zero() else answer
print(result)