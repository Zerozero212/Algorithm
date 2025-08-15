from collections import deque
def solution(numbers, target):
    answer = 0
    q=deque([(0,0)])
    while q:
        idx,sum = q.popleft()
        if idx==len(numbers) and sum == target: answer += 1
        if idx < len(numbers):
            q.append((idx+1,sum+numbers[idx]))
            q.append((idx+1,sum-numbers[idx]))
    return answer