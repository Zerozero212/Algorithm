from collections import Counter
N=int(input())
arr=list(map(int,input().split()))
M=int(input())
search_num = list(map(int,input().split()))

arr=Counter(arr)
for n in search_num:
    print(arr[n],end=" ")