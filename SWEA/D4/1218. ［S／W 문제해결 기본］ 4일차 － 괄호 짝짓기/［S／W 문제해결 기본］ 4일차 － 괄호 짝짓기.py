def sol():
    s=[]
    l={'(':1,'{':2,'[':3,'<':4}
    r={')':1,'}':2,']':3,'>':4}
    for ch in arr:
        if ch in l: s.append(ch)
        elif not s: return 0
        else: 
            tmp=s.pop()
            if r[ch]!=l[tmp]: return 0
    if s: return 0
    return 1


for t in range(1,11):
    N=int(input())
    arr=list(input())
    print(f'#{t} {sol()}')