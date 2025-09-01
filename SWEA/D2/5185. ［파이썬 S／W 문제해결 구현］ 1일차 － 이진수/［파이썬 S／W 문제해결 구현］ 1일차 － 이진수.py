T=int(input())
for t in range(1,T+1):
    lst = input().split()
    num=int(lst[1],16)
    arr=[]
    while num:
        arr.append(str(num%2))
        num//=2
    print(f"#{t} {''.join(['0']*(4*int(lst[0])-len(arr)) + arr[::-1])}")