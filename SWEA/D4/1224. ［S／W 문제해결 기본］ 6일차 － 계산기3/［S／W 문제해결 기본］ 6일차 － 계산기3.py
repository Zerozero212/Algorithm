def sol(idx):
    idx+=1
    stack=[]
    tmp_ope=[]
    while arr[idx]!=')':
        if arr[idx].isdigit(): stack.append(arr[idx])
        elif arr[idx]=='(':
            idx,tmp_stack=sol(idx)
            stack.extend(tmp_stack)
        else: 
            while tmp_ope and pri[tmp_ope[-1]]>=pri[arr[idx]]:
                stack.append(tmp_ope.pop())
            tmp_ope.append(arr[idx])
        idx+=1
    while tmp_ope:
        stack.append(tmp_ope.pop())
    return idx,stack

for t in range(1,11):
    N=int(input())
    arr=list(input())
    stack=[]
    ope=[]
    pri={'+':1,'*':2}
    
    idx=0
    while idx<N:
        if arr[idx].isdigit(): stack.append(arr[idx])
        elif arr[idx]=='(': 
            idx,tmp_stack=sol(idx)
            stack.extend(tmp_stack)
        else:
            while ope and pri[ope[-1]]>=pri[arr[idx]]:
                stack.append(ope.pop())
            ope.append(arr[idx])
        idx+=1
    
    while ope:
        stack.append(ope.pop())
    
    output=[]
    for ch in stack:
        if ch.isdigit(): output.append(int(ch))
        elif ch=='+': output.append(output.pop()+output.pop())
        else: output.append(output.pop()*output.pop())
    print(f'#{t} {output[0]}')