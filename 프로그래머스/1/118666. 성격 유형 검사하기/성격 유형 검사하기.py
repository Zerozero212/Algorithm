# 성격 유형 점수를 더함 > 더 높은 점수를 받은 성격 유형 당첨
# 단, 하나의 지표에서 유형 점수가 같다면, 사전 순!

def solution(survey, choices):
    std='RTCFJMAN'
    score=[0]*8
    for i in range(len(survey)):
        if choices[i] == 4: continue
        elif choices[i] < 4:
            score[std.index(survey[i][0])] += 4-choices[i]
        else:
            score[std.index(survey[i][1])] += choices[i]-4
    
    ans=''
    for i in range(0,8,2):
        if score[i]>=score[i+1]: ans+=std[i]
        else: ans+=std[i+1]
    
    return ans