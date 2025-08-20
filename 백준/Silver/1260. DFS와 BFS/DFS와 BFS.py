from collections import deque
import sys
input=sys.stdin.readline

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += reversed(graph[n])
    return visited

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n]
    return visited

node,edge,root_node=map(int,input().split())
graph_list={i:[] for i in range(1,node+1)}
for i in range(1,edge+1):
    node1,node2=map(int,input().split())
    graph_list[node1].append(node2)
    graph_list[node2].append(node1)

for key in graph_list:
    graph_list[key].sort()

for ch in DFS_with_adj_list(graph_list, root_node):
    print(ch,end=' ')
print()
for ch in BFS_with_adj_list(graph_list, root_node):
    print(ch,end=' ')