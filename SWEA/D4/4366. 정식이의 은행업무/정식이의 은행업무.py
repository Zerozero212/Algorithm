def valid(n_str,num):
    arr = []
    for i in range(len(n_str)):
        for idx in range(num):
            if n_str[i] != idx: 
                temp = n_str[:]
                temp [i] = idx
                arr.append(int(''.join(map(str,temp)),num))
    return set(arr)

T = int(input())
for tc in range(1,T+1):
    two = list(map(int,input()))
    three = list(map(int,input()))
    print(f'#{tc} {(set(valid(two,2)) & set(valid(three,3))).pop()}')