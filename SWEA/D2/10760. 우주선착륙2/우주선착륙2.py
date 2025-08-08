def cnt(arr1,n,m):
    direct = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    count = 0
    for x in range(n):
        for y in range(m):
            temp = 0
            for dx, dy in direct:
                if 0 <= x+dx < n and 0 <= y+dy < m and arr1[x+dx][y+dy] < arr1[x][y]: temp += 1
            if temp >= 4: count += 1
    return count

T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{t} {cnt(arr,N,M)}')
