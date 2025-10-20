from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for u,v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs():
        q = deque([(0,1)])
        v=[0]*(n+1)
        cnt_list = [0]*(n+1)
        
        while q:
            cnt,node = q.popleft()
            if v[node]: continue
            v[node]=1
            cnt_list[node]=cnt
            for nxt_node in graph[node]:
                if v[nxt_node]: continue
                q.append((cnt+1,nxt_node))
        return cnt_list
    
    cnt_list = bfs()
    
    return cnt_list.count(max(cnt_list))