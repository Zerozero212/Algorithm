for t in range(1,11):
    N=int(input())
    stack=[]
    value=[0]*(N+1)
    for _ in range(N):
        tmp=input().split()
        if tmp[1].isdigit():
            value[int(tmp[0])]=int(tmp[1])
        else:
            value[int(tmp[0])]=tmp[1]
            stack.append((int(tmp[0]),int(tmp[2]),int(tmp[3])))
    while stack:
        idx,n1,n2=stack.pop()
        if value[idx]=='+': value[idx]=value[n1]+value[n2]
        elif value[idx]=='-': value[idx]=value[n1]-value[n2]
        elif value[idx]=='*': value[idx]=value[n1]*value[n2]
        else: value[idx]=value[n1]//value[n2]
    print(f'#{t} {value[1]}')