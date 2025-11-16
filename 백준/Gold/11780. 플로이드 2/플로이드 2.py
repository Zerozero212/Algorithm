import sys
input = sys.stdin.readline
INF = 10**9

N = int(input())
M = int(input())
costs = [[INF]*N for _ in range(N)]
paths = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    u,v,w = map(int,input().split())
    if w < costs[u-1][v-1]:
        costs[u-1][v-1]=w
        paths[u-1][v-1]=[u,v]

for i in range(N):
    costs[i][i]=0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if costs[i][j] > costs[i][k] + costs[k][j]:
                costs[i][j] = costs[i][k] + costs[k][j]
                paths[i][j] = paths[i][k] + paths[k][j][1:]

for i in range(N):
    for j in range(N):
        if costs[i][j]==INF:
            print(0,end=' ')
        else:
            print(costs[i][j],end=' ')
    print()

for i in range(N):
    for j in range(N):
        path_len = len(paths[i][j])
        if path_len:
            print(path_len,end=' ')
            print(*paths[i][j])
        else:
            print(path_len)