from heapq import heappush, heappop

T = int(input())
arr = []
num = [int(input()) for _ in range(T)]

for n in num:
    if n:
        heappush(arr,-1*n)
    else:
        print(-1*heappop(arr) if arr else 0)