from collections import deque

def merge(li1, li2):
    ans = []
    while li1 and li2:
        if li1[0] < li2[0]:
            ans.append(li1.popleft())
        else:
            ans.append(li2.popleft())
    if li1: ans.extend(li1)
    if li2: ans.extend(li2)
    return ans

def merge_sort(l, r):
    global cnt
    if l == r:
        return [arr[l]]
    mid = (l + r + 1) // 2        
    left = merge_sort(l, mid-1)
    right = merge_sort(mid, r)
    if left[-1] > right[-1]:
        cnt += 1
    return merge(deque(left), deque(right))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(0, N-1)
    print(f'#{tc} {ans[N//2]} {cnt}')
