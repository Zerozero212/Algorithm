import sys
input = sys.stdin.readline
from itertools import accumulate
N,M=map(int,input().split())
arr=list(accumulate([0]+list(map(int,input().split()))))

for _ in range(M):
    s,e=map(int,input().split())
    print(arr[e]-arr[s-1])