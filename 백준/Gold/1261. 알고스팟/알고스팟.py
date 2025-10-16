from heapq import heappush,heappop
dir1 = [(0,1),(0,-1),(1,0),(-1,0)]
def daijckstra():
    costs = [[1e9]*M for _ in range(N)]
    costs[0][0]=0
    heap = [(0,0,0)]

    while heap:
        cnt,x,y = heappop(heap)
        
        if costs[x][y] < cnt: continue
        if (x,y)==(N-1,M-1): return cnt
        
        for dx,dy in dir1:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<M:
                new_cnt=cnt
                if maze[nx][ny]:
                    new_cnt += 1
                if new_cnt < costs[nx][ny]:
                    costs[nx][ny]=new_cnt
                    heappush(heap,(new_cnt,nx,ny))

M,N = map(int,input().split())
maze = [list(map(int,list(input()))) for _ in range(N)]
print(daijckstra())