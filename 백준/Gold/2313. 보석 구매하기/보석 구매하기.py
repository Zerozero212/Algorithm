c = 0               # 전체 보석 가치 총합
LR = []             # 각 줄에서 (시작, 끝) 인덱스를 저장
for _ in range(int(input())):
    n = int(input())                   # 한 줄에 있는 보석 개수
    L = list(map(int,input().split())) # 보석 가치 리스트
    l, r = 0, 0                        # 현재 줄에서 최대 구간의 (왼쪽, 오른쪽) 인덱스
    dp = [0]*n                         # 각 위치까지의 최대 연속합 저장
    dp[0] = L[0]
    
    m = L[0]        # 현재 줄에서의 최대 부분합
    x = 0           # 현재 구간의 시작 인덱스 후보
    for i in range(1,n):
        if dp[i-1] <= 0:
            dp[i] = L[i]
            x = i
            if L[i] > m or (L[i] == m and r-l > 0):
                l,r = i,i
        else:
            dp[i] = dp[i-1]+L[i]
            if dp[i] > m or (dp[i] == m and r-l > i-x):
                l,r = x,i
        m = max(m,dp[i])
    
    c += m
    LR.append([l+1,r+1])
print(c)
for i in LR:
    print(*i)