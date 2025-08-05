# incr : num이 단조증가하는 숫자인지 확인하는 함수
def incr(num):
    # num이 123이라면 [1, 2, 3]로 만드는 작업 123 > '123' > 1 2 3 > [1, 2, 3]
    num_arr = list(map(int,str(num)))
    for i in range(1,len(num_arr)):
        if num_arr[i-1] > num_arr[i]: return 0
    return 1

def valid(arr1):
    max = -1
    for i in range(len(arr1)):
        # i<j이기에 j는 시작점이 i+1
        for j in range(i+1,len(arr1)):
            temp = arr1[i] * arr1[j]
            if incr(temp):
                if max < temp: max = temp
    return max

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f'#{t} {valid(arr)}')
