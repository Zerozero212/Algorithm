import sys
input = sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
M=int(input())
search_num = list(map(int,input().split()))

card=dict()
for n in arr:
    if n in card: card[n]+=1
    else: card[n]=1

result=[]
for n in search_num:
    if n in card: result.append(card[n])
    else: result.append(0)

print(*result)