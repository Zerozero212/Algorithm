def solution(numbers, target):
    cnt = 0

    def dfs(idx,total,sum,t):
        nonlocal cnt
        if idx==total:
            if sum == t: cnt += 1
            return
        
        dfs(idx+1,total,sum+numbers[idx],t)
        dfs(idx+1,total,sum-numbers[idx],t)

    dfs(0,len(numbers),0,target)
    return cnt