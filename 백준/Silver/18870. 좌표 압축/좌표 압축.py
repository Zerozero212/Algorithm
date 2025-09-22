import sys
input = sys.stdin.readline

N=int(input())
arr = list(map(int,input().split()))
table = {v:i for i,v in enumerate(sorted(set(arr)))}

for n in arr:
    print(table[n],end=" ")