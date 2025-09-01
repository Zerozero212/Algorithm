dir1=[(0,1),(1,0)]
def dfs(x,y,sum):
    global min_num
    if sum>min_num: return
    if (x,y)==(N-1,N-1): min_num=sum
    for dx,dy in dir1:
        nx,ny=x+dx,y+dy
        if 0<=nx<N and 0<=ny<N: dfs(nx,ny,sum+arr[nx][ny])

T=int(input())
for t in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    min_num=float('inf')
    dfs(0,0,arr[0][0])
    print(f'#{t} {min_num}')