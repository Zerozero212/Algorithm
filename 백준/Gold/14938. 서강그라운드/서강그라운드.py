import sys
input = sys.stdin.readline
INF = 10**9

n,m,r = map(int,input().split())
items = list(map(int,input().split()))

paths = [[INF]*n for _ in range(n)]

for _ in range(r):
    u,v,w = map(int,input().split())
    paths[u-1][v-1] = w
    paths[v-1][u-1] = w

for i in range(n):
    paths[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if paths[i][j] > paths[i][k] + paths[k][j]:
                paths[i][j] = paths[i][k] + paths[k][j]

ans=0
for i in range(n):
    tmp = 0
    for j in range(n):
        if paths[i][j] <= m:
            tmp += items[j]
    ans = max(ans,tmp)

print(ans)