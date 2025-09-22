import sys
input = sys.stdin.readline
from collections import Counter

N=int(input())
arr = list(map(int,input().split()))
table = {v:i for i,v in enumerate(Counter(sorted(arr)).keys())}

for n in arr:
    print(table[n],end=" ")