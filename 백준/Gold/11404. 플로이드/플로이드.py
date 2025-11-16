N = int(input())
M = int(input())
costs=[[0]*N for _ in range(N)]

for _ in range(M):
    u,v,w = map(int,input().split())
    
    if costs[u-1][v-1] == 0 or w < costs[u-1][v-1]:
        costs[u-1][v-1] = w

for k in range(N):
    for i in range(N):
        if k==i: continue
        for j in range(N):
            if i==j or k==j: continue
            if 0 in (costs[i][k],costs[k][j]): continue
            
            tmp = costs[i][k]+costs[k][j]
            if costs[i][j]==0 or tmp < costs[i][j]: 
                costs[i][j] = tmp

for row in costs:
    print(*row)