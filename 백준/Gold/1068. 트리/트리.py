def search_tree(node):
    global ans
    if len(tree[node])==0:
        ans+=1
        return
    for nxt_node in tree[node]:
        search_tree(nxt_node)

N=int(input())
prev=list(map(int,input().split()))
tree=[[] for _ in range(N)]
target=int(input())
prev[target]=-2

if -1 in set(prev):
    root = prev.index(-1)

    cut_list=set((target,))

    for i in range(N):
        if prev[i]>=0:
            if prev[i] in cut_list:
                cut_list.add(i)
            else:
                tree[prev[i]].append(i)

    ans=0
    search_tree(root)
    print(ans)
else:
    print(0)