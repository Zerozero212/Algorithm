def inorder(n):
    if n>N: return
    inorder(2*n)
    ans.append(tree[n])
    inorder(2*n+1)

for t in range(1,11):
    N=int(input())
    tree=[0]*(N+1)
    for _ in range(N):
        tmp=input().split()
        tree[int(tmp[0])]=tmp[1]
    ans=[]
    inorder(1)
    print(f"#{t} {''.join(ans)}")