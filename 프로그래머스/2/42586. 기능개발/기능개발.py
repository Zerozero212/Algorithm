import math

def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    answer = []
    cur_day = days[0]  
    cnt = 1
    
    for d in days[1:]:
        if d <= cur_day:
            cnt += 1
        else:
            answer.append(cnt)
            cur_day = d
            cnt = 1
    answer.append(cnt)
    return answer
