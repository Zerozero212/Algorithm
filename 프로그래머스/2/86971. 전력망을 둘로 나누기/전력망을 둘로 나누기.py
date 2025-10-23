from collections import deque

def solution(n, wires):
    ans=1e9
    for i in range(n-1):
        arr = wires[:i] + wires[i+1:]
        graph=[[] for _ in range(n+1)]
        for u,v in arr:
            graph[u].append(v)
            graph[v].append(u)
        
        v=[0]*(n+1)
        
        q=deque([arr[0][0]])
        tmp_cnt=0
        while q:
            num = q.popleft()
            if v[num]: continue
            v[num]=1
            tmp_cnt+=1     
            
            for nxt in graph[num]:
                if v[nxt]: continue
                q.append(nxt)
        
        ans = min(ans,abs(2*tmp_cnt - n))
        
        if not ans: break
        
    return ans