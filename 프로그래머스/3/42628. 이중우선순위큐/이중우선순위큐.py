from heapq import heappush,heappop

def solution(operations):
    pq=[]
    for operation in operations:
        ch,num = operation.split()
        if ch=='I':
            heappush(pq,int(num))
        elif operation=='D 1':
            if pq: pq.remove(max(pq))
        elif operation=='D -1':
            if pq: heappop(pq)
    
    if pq: return [max(pq),min(pq)]
    return [0,0]