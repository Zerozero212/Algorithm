def sol(num,cnt,path):
    if cnt==M:
        print(*path)
        return
    
    for i in range(num,N+1):
        sol(i,cnt+1,path+[i])

N,M = map(int,input().split())
sol(1,0,[])