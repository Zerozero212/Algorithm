T = int(input())

for t in range(1,T+1):
    N = int(input())
    st = [0]*5001

    for _ in range(N):
        A,B = map(int,input().split())
        for i in range(A,B+1):
            st[i] += 1
    
    P = int(input())
    st_li = [int(input()) for _ in range(P)]
    answer = [st[x] for x in st_li]
    print(f'#{t}', *answer)