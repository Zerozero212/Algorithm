def bfs(s):
    q=[s]
    cnt=0
    while q:
        n=q.pop(0)
        cnt+=1
        for num in tree[n]: q.append(num)
    return cnt

T=int(input())
for t in range(1,T+1):
    E,R=map(int,input().split())
    arr=list(map(int,input().split()))
    tree=[[] for _ in range(E+2)]
    for i in range(0,2*E,2):
        tree[arr[i]].append(arr[i+1])
    print(f'#{t} {bfs(R)}')