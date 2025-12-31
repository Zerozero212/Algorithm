N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
coor = [list(map(int,input().split())) for _ in range(M)]

arr2 = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i-1 >= 0: arr2[i][j] += arr2[i-1][j]
        if j-1 >= 0: arr2[i][j] += arr2[i][j-1]
        if i-1 >= 0 and j-1 >= 0: arr2[i][j] -= arr2[i-1][j-1]
        arr2[i][j] += arr[i][j]

for x1,y1,x2,y2 in coor:
    x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
    ans = arr2[x2][y2]
    if x1-1 >= 0:
        ans -= arr2[x1-1][y2]
    if y1-1 >= 0:
        ans -= arr2[x2][y1-1]
    if x1-1 >= 0 and y1-1 >= 0:
        ans += arr2[x1-1][y1-1]
    print(ans)