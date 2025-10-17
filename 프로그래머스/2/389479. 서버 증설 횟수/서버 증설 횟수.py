def solution(players, m, k):
    
    def make_server(s,k,cnt):
        e=s+k
        
        if e > 24:
            e = 24
            
        for i in range(s,e):
            server[i]+=cnt
    
    ans=0
    server=[0]*24
    N=len(players)
    
    for i in range(N):
        if players[i]//m <= server[i]: continue
        need_server_cnt = players[i]//m - server[i]
        make_server(i,k,need_server_cnt)
        ans+=need_server_cnt
    
    return ans