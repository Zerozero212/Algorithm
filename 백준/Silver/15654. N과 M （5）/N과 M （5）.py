def sol(cnt,path):
    if cnt==M:
        print(*path)
        return
    
    for i in range(N):
        if v[i]: continue
        v[i]=1
        sol(cnt+1,path+[arr[i]])
        v[i]=0

N,M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
v=[0]*N
sol(0,[])