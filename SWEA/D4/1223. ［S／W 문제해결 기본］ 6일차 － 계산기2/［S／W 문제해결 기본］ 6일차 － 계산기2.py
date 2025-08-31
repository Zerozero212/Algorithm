for t in range(1,11):
    N=int(input())
    arr=list(input())
    num=[]
    stack=[]
    idx=0
    while idx<N:
        if arr[idx]=='*':
            arr[idx],arr[idx+1]=arr[idx+1],arr[idx]
            idx+=2
        else: idx+=1
    
    idx=0
    while idx<N:
        if arr[idx]=='+':
            tmp=idx
            idx+=1
            while idx<N and arr[idx]!='+':
                num.append(arr[idx])
                idx+=1
            num.append('+')
        else:
            num.append(arr[idx])
            idx+=1
    for n in num:
        if n.isdigit(): stack.append(int(n))
        elif n=='*': stack.append(stack.pop()*stack.pop())
        elif n=='+': stack.append(stack.pop()+stack.pop())
    print(f'#{t} {stack[0]}')