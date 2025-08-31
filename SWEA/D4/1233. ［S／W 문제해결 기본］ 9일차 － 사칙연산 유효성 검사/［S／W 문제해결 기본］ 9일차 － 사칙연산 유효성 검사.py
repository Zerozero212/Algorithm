def post(v):
    global ans
    if 2*v>n:
        if not tree[v].isdigit():
            ans=0
        return
    if 2*v<n:
        if tree[v].isdigit():
            ans=0
            return
    post(2*v)
    post(2*v+1)

for t in range(1,11):
    n=int(input())
    ans=1
    tree=[0]*(n+1)
    for _ in range(n):
        tmp=input().split()
        tree[int(tmp[0])]=tmp[1]
    if not n%2: 
        print(f'#{t} 0')
        continue
    post(1)
    print(f'#{t} {ans}')