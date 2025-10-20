import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    # 1. 인덱스 붙이기
    nodes = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]

    # 2. y 내림차순, x 오름차순 정렬 (루트가 맨 위로)
    nodes.sort(key=lambda n: (-n[1], n[0]))

    # 3. 트리 구성 (딕셔너리로 자식 관리)
    tree = {idx: [None, None] for _, _, idx in nodes}
    root = nodes[0]

    for x, y, idx in nodes[1:]:
        parent_x, parent_y, parent_idx = root
        cur = root
        while True:
            if x < cur[0]:
                # 왼쪽 자식
                left = tree[cur[2]][0]
                if left is None:
                    tree[cur[2]][0] = (x, y, idx)
                    break
                else:
                    cur = left
            else:
                # 오른쪽 자식
                right = tree[cur[2]][1]
                if right is None:
                    tree[cur[2]][1] = (x, y, idx)
                    break
                else:
                    cur = right

    # 4. 전위 순회
    preorder_result = []
    def preorder(node):
        if node is None:
            return
        preorder_result.append(node[2])
        preorder(tree[node[2]][0])
        preorder(tree[node[2]][1])

    # 5. 후위 순회
    postorder_result = []
    def postorder(node):
        if node is None:
            return
        postorder(tree[node[2]][0])
        postorder(tree[node[2]][1])
        postorder_result.append(node[2])

    preorder(root)
    postorder(root)

    # 6. 반환
    answer = [preorder_result, postorder_result]
    return answer
