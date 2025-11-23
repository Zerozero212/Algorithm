from collections import deque
dir1 = [(0,1),(0,-1),(1,0),(-1,0)]

def sol():
    while my_pos:
        f_num = len(fire_pos)
        m_num = len(my_pos)
        for _ in range(f_num):
            fx,fy = fire_pos.popleft()
            for dx,dy in dir1:
                nfx,nfy = fx+dx, fy+dy
                if 0<=nfx<N and 0<=nfy<M and maze[nfx][nfy] not in '#*':
                    maze[nfx][nfy] = '*'
                    fire_pos.append((nfx,nfy))

        for _ in range(m_num):
            cnt,mx,my = my_pos.popleft()
            if mx in (0,N-1) or my in (0,M-1): return cnt+1
            for dx,dy in dir1:
                nmx,nmy = mx+dx,my+dy
                if 0<=nmx<N and 0<=nmy<M and maze[nmx][nmy]=='.':
                    maze[nmx][nmy] = '@'
                    my_pos.append((cnt+1,nmx,nmy))
        
    return 'IMPOSSIBLE'

T = int(input())
for _ in range(T):
    M,N = map(int,input().split())
    maze = [list(input()) for _ in range(N)]

    fire_pos = deque()
    my_pos = deque()

    for i in range(N):
        for j in range(M):
            if maze[i][j]=='@': my_pos.append((0,i,j))
            elif maze[i][j]=='*': fire_pos.append((i,j))

    print(sol())