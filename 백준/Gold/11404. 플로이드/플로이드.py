import sys
input = sys.stdin.readline
INF = 1e9

N = int(input())
M = int(input())

costs = [[INF]*N for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    costs[u-1][v-1] = min(costs[u-1][v-1], w)

for k in range(N):
    for i in range(N):

        if k==i: continue

        for j in range(N):
            if k==j or i==j: continue
            if costs[i][j] > costs[i][k] + costs[k][j]:
                costs[i][j] = costs[i][k] + costs[k][j]

for i in range(N):
    for j in range(N):
        if costs[i][j] == INF:
            print(0, end=' ')
        else:
            print(costs[i][j], end=' ')
    print()