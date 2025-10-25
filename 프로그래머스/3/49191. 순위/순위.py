def solution(n, results):
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    
    for w,l in results:
        win[w].append(l)
        lose[l].append(w)
    
    def win_dfs(std,num):
        for idx in win[num]:
            if v_win[idx]: continue
            v_win[idx]=1
            win[std].append(idx)
            win_dfs(std,idx)
    
    def lose_dfs(std,num):
        for idx in lose[num]:
            if v_lose[idx]: continue
            v_lose[idx]=1
            lose[std].append(idx)
            lose_dfs(std,idx)
    
    for i in range(1,n+1):
        v_win=[0]*(n+1)
        v_lose=[0]*(n+1)
        
        v_win[i]=1
        v_lose[i]=1
        
        for num in win[i]:
            v_win[num]=1
            win_dfs(i,num)
        
        for num in lose[i]:
            v_lose[num]=1
            lose_dfs(i,num)
    
    ans=0
    for i in range(1,n+1):
        if len(set(win[i]))+len(set(lose[i]))==n-1:
            ans+=1
    
    return ans