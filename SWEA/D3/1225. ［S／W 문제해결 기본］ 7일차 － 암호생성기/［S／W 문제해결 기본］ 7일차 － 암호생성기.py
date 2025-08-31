def sol(lst):
    while 1:
        for i in range(1,6):
            tmp = lst.pop(0)-i
            if tmp<=0: return lst+[0]
            lst.append(tmp)

for t in range(1,11):
    a=input()
    arr=list(map(int,input().split()))
    print(f'#{t} ',*sol(arr))