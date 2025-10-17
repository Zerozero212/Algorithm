from heapq import heappush,heappop

def solution(n, s, a, b, fares):
    
    def daijckstra(start):
        costs = [10**18]*(n+1)
        costs[start]=0
        pq = [(0,start)]

        while pq:
            c,node = heappop(pq)
            if costs[node] < c: continue

            for nxt_c,nxt_node in graph[node]:
                new_c = c+nxt_c
                if new_c < costs[nxt_node]:
                    costs[nxt_node]=new_c
                    heappush(pq,(new_c,nxt_node))

        return costs
    
    graph=[[] for _ in range(n+1)]
    for u,v,c in fares:
        graph[u].append((c,v))
        graph[v].append((c,u))
    
    from_s = daijckstra(s)
    from_a = daijckstra(a)
    from_b = daijckstra(b)
    
    ans = min(from_s[i] + from_a[i] + from_b[i] for i in range(1,n+1))

    return ans