import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    nodes = [(idx+1,x,y) for idx,(x,y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda n: (-n[2],n[1]))
    tree = {idx+1 : [None,None] for idx in range(len(nodes))}
    root = nodes[0]

    for idx,x,y in nodes[1:]:
        cur = root
        while True:
            if x<cur[1]:
                left = tree[cur[0]][0]
                if left:
                    cur=left
                    continue
                else:
                    tree[cur[0]][0] = (idx,x,y)
                    break
            else:
                right = tree[cur[0]][1]
                if right:
                    cur=right
                    continue
                else:
                    tree[cur[0]][1] = (idx,x,y)
                    break
    
    def pre_order(node):
        if node is None: return
        pre_order_path.append(node[0])
        pre_order(tree[node[0]][0])
        pre_order(tree[node[0]][1])

    def post_order(node):
        if node is None: return
        post_order(tree[node[0]][0])
        post_order(tree[node[0]][1])
        post_order_path.append(node[0])

    pre_order_path = []
    post_order_path = []
    pre_order(root)
    post_order(root)
    answer = [pre_order_path,post_order_path]
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))