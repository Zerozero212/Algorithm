N,M = map(int,input().split())
INF = 1e9
graph = [[INF]*N for _ in range(N)]
paths = [[[] for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u-1][v-1] = w
    graph[v-1][u-1] = w
    paths[u-1][v-1] = [u,v]
    paths[v-1][u-1] = [v,u]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                paths[i][j] = paths[i][k] + paths[k][j][1:]

for i in range(N):
    for j in range(N):
        if i==j:
            print('-',end=' ')
        else:
            print(paths[i][j][1],end=' ')
    print()