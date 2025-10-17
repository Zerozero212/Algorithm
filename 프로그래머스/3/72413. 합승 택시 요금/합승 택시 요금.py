from heapq import heappush,heappop

def solution(n, s, a, b, fares):
    
    def daijckstra(n,start,end=0):
        costs = [10**18]*(n+1)
        costs[start]=0
        pq = [(0,start)]

        while pq:
            c,n = heappop(pq)
            if costs[n] < c: continue
            if n==end: return c

            for nxt_c,nxt_n in graph[n]:
                new_c = c+nxt_c
                if new_c < costs[nxt_n]:
                    costs[nxt_n]=new_c
                    heappush(pq,(new_c,nxt_n))
        if end: return 10**18
        return costs
    
    graph=[[] for _ in range(n+1)]
    for u,v,c in fares:
        graph[u].append((c,v))
        graph[v].append((c,u))
    
    sub_cost = daijckstra(n,s)
    ans = 10**18
    for i in range(1,n+1):
        if ans < sub_cost[i]: continue
        tmp_ans = sub_cost[i] + daijckstra(n,i,a) + daijckstra(n,i,b)
        if tmp_ans < ans: 
            ans = tmp_ans
    
    return ans