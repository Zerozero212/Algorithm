def solution(numbers):
    ans = set()
    N=len(numbers)
    for i in range(N-1):
        for j in range(i+1,N):
            ans.add(numbers[i]+numbers[j])
    return sorted(list(ans))