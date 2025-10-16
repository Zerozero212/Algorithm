def sol(cnt,path):
    if cnt==M:
        print(*path)
        return

    for i in range(1,N+1):
        sol(cnt+1,path+[i])

N,M = map(int,input().split())
sol(0,[])