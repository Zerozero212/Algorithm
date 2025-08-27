import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    cnt = 0  

    for i in range(1, n + 1):
        if visited[i]:
            continue
        stack = []
        cur = i
        while True:
            if visited[cur]:
                if cur in stack:
                    idx = stack.index(cur)
                    cnt += len(stack) - idx
                break
            visited[cur] = True
            stack.append(cur)
            cur = arr[cur]

    print(n - cnt)
