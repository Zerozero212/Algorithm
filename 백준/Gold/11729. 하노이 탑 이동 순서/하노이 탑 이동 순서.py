def hanoi_cnt(n,s,m,e):
    global cnt
    cnt+=1
    if n==1:
        return
    hanoi_cnt(n-1,s,e,m)
    hanoi_cnt(n-1,m,s,e)

def hanoi(n,s,m,e):
    if n==1:
        print(s,e)
        return
    hanoi(n-1,s,e,m)
    print(s,e)
    hanoi(n-1,m,s,e)

N=int(input())
cnt=0
hanoi_cnt(N,1,2,3)
print(cnt)
hanoi(N,1,2,3)