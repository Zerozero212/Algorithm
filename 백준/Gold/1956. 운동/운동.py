V,E = map(int,input().split())
INF = 1e9
paths = [[INF]*V for _ in range(V)]

for _ in range(E):
    u,v,w = map(int,input().split())
    paths[u-1][v-1] = w

for k in range(V):
    for i in range(V):
        for j in range(V):
            if paths[i][j] > paths[i][k] + paths[k][j]:
                paths[i][j] = paths[i][k] + paths[k][j]

ans = INF
for i in range(V):
    ans = min(ans,paths[i][i])

print(ans if ans!=INF else -1)