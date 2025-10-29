def solution(n):
    diag1=[0]*(2*n-1)
    diag2=[0]*(2*n-1)
    col=[0]*n
    
    ans=0
    def dfs(row,cnt):
        nonlocal ans
        if cnt==n: 
            ans+=1
            return
        if row>=n: return
        
        for i in range(n):
            if col[i] or diag1[row+i] or diag2[i-row]: continue
            col[i]=diag1[row+i]=diag2[i-row]=1
            dfs(row+1,cnt+1)
            col[i]=diag1[row+i]=diag2[i-row]=0
    
    dfs(0,0)
    return ans

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    print(f'#{tc} {solution(N)}')