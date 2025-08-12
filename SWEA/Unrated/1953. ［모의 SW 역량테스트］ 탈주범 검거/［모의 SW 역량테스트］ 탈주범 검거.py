from collections import deque
tunnel_type = [[],[(-1,0),(1,0),(0,-1),(0,1)],[(-1,0),(1,0)],[(0,-1),(0,1)],[(-1,0),(0,1)],[(1,0),(0,1)],[(1,0),(0,-1)],[(-1,0),(0,-1)]]

def bfs(x,y,time):
    total = 0
    q = deque([(x,y,time)])
    while q:
        i,j,t = q.popleft()
        if t == 0: break
        total += 1
        for dx, dy in tunnel_type[arr[i][j]]:
            nx,ny = i+dx, j+dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny]: 
                if (i,j) in [(nx + dx2,ny + dy2) for dx2, dy2 in tunnel_type[arr[nx][ny]]]:
                    if (nx,ny,t-1) not in q: q.append((nx,ny,t-1))
        arr[i][j] = 0 
    return total

T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc} {bfs(R,C,L)}')