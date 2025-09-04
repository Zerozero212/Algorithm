def dfs(cnt):
    global ans
    tmp=(cnt,''.join(N))
    if tmp in v: return
    v.add(tmp)
 
    if cnt==K:
        ans=max(ans,int(''.join(N)))
        return
    for i in range(len(N)-1):
        for j in range(i+1,len(N)):
            N[i],N[j]=N[j],N[i]
            dfs(cnt+1)
            N[j],N[i]=N[i],N[j]
 
T=int(input())
for tc in range(1,T+1):
    N,K=input().split()
    N=list(N)
    K=int(K)
    ans=float('-inf')
    v=set()
 
    dfs(0)
    print(f"#{tc} {ans}")