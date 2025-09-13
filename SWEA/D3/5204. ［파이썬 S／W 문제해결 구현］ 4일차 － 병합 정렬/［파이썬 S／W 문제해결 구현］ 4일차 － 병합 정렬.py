def merge(li1,li2):
    ans=[]
    idx_1=idx_2=0
    while idx_1<len(li1) and idx_2<len(li2):
        if li1[idx_1]<li2[idx_2]: 
            ans.append(li1[idx_1])
            idx_1+=1
        else: 
            ans.append(li2[idx_2])
            idx_2+=1

    if idx_1<len(li1): ans.extend(li1[idx_1:])
    if idx_2<len(li2): ans.extend(li2[idx_2:])
    return ans

def merge_sort(li):
    global cnt
    if len(li)==1: return li
    mid=len(li)//2
    left=merge_sort(li[:mid])
    right=merge_sort(li[mid:])
    if left[-1]>right[-1]: cnt+=1
    return merge(left,right)

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    cnt=0
    arr=merge_sort(list(map(int,input().split())))
    print(f'#{tc} {arr[N//2]} {cnt}')