for t in range(1,11):
    N=input()
    s=list(map(int,input().replace('+',' ').split()))
    while len(s)>1:
        s.append(s.pop()+s.pop())
    print(f'#{t} {s[0]}')