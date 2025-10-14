from heapq import heappush, heappop

N = int(input())
lesson = [tuple(map(int, input().split())) for _ in range(N)]
lesson.sort()  

heap = []  

for s, e in lesson:
    if heap and heap[0] <= s:
        heappop(heap)
    heappush(heap, e)

print(len(heap))