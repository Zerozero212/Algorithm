# 성격 유형 점수를 더함 > 더 높은 점수를 받은 성격 유형 당첨
# 단, 하나의 지표에서 유형 점수가 같다면, 사전 순!

def solution(survey, choices):
    std = 'RTCFJMAN'
    idx = {c:i for i,c in enumerate(std)}
    score = [0]*8
    
    for s, c in zip(survey, choices):
        if c == 4: continue
        if c < 4:
            score[idx[s[0]]] += 4 - c
        else:
            score[idx[s[1]]] += c - 4
    
    ans=''
    for i in range(0,8,2):
        if score[i]>=score[i+1]: ans+=std[i]
        else: ans+=std[i+1]
    
    return ans