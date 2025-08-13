from collections import deque
dir1 = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(p,f):
    person_q = deque([p])
    fire_q = deque([*f])
    while person_q:
        for _ in range(len(fire_q)):
            i,j,t = fire_q.popleft()
            for di,dj in dir1:
                ni,nj = i+di,j+dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] in '.@':
                    arr[ni][nj] = '*'
                    fire_q.append((ni,nj,t+1))
        for _ in range(len(person_q)):
            i,j,t = person_q.popleft()
            if i in [0,N-1] or j in [0,M-1]: return t+1
            for di,dj in dir1:
                ni,nj = i+di,j+dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '.':
                    arr[ni][nj] = '@'
                    person_q.append((ni,nj,t+1))
    return 'IMPOSSIBLE'

T = int(input())
for tc in range(T):
    M,N = map(int,input().split())
    arr = []
    person_x = person_y = 0
    fire_idx_list = []

    for i in range(N):
        temp = list(input())
        for j in range(M):
            if temp[j] == '@': person_x,person_y = i,j
            if temp[j] == '*': fire_idx_list.append((i,j,0))
        arr.append(temp)

    print(bfs((person_x,person_y,0),fire_idx_list))