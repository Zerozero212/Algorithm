def sol():
    q=[0]
    while q:
        node=q.pop(0)
        for num in tree[node]:
            if num==99: return 1
            q.append(num)
    return 0

for t in range(1,11):
    tc,E=map(int,input().split())
    arr=list(map(int,input().split()))
    tree=[[] for _ in range(99)]
    for i in range(0,2*E,2):
        tree[arr[i]].append(arr[i+1])
    print(f'#{t} {sol()}')