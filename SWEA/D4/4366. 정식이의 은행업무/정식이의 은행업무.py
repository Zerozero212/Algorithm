def valid(n_str,num):
    arr = []
    for i in range(len(n_str)):
        for idx in range(num):
            if n_str[i] != idx: # 처음에 202에서 212만 고려하고, 222와 같이 2씩 바뀌는 것을 고려하지 못함
                temp = n_str[:]
                temp [i] = idx
                arr.append(int(''.join(map(str,temp)),num)) # int(문자열, 숫자) > 문자열을 10진법으로 변경
    return set(arr)

T = int(input())
for tc in range(1,T+1):
    two = list(map(int,input()))
    three = list(map(int,input()))
    print(f'#{tc} {(set(valid(two,2)) & set(valid(three,3))).pop()}')
