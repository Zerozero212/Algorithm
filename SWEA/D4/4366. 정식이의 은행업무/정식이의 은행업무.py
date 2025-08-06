def tr(num_list,num1):
    t = 0
    for i in range(len(num_list)):
        t += num_list[i]*num1**(len(num_list)-i-1)
    return t

def valid(n_str,num):
    arr = []
    for i in range(len(n_str)):
        for idx in range(num):
            if n_str[i] != idx: 
                temp = n_str[:]
                temp [i] = idx
                arr.append(tr(temp,num))
    return set(arr)

T = int(input())
for tc in range(1,T+1):
    two = list(map(int,input()))
    three = list(map(int,input()))
    print(f'#{tc} {(set(valid(two,2)) & set(valid(three,3))).pop()}')