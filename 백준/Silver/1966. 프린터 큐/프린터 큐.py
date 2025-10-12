from collections import deque
T=int(input())
for _ in range(T):
    N,target_idx = map(int,input().split())
    arr = list(map(int,input().split()))
    rotation = deque([(value,idx) for idx,value in enumerate(arr)])
    std = max(rotation)
    cnt=0

    while True:
        v,i = rotation.popleft()
        if i==target_idx and v==std[0]:
            print(cnt+1)
            break
        elif v==std[0]:
            cnt+=1
            std=max(rotation)
            continue
        rotation.append((v,i))