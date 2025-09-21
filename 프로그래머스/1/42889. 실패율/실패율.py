def solution(N, stages):
    answer = []
    user=[0]*(N+1)
    
    for stage in stages:
        if stage > N: stage=N
        for i in range(1,stage+1):
            user[i]+=1

    for i in range(1,N+1):
        if not user[i]: continue
        user[i]=stages.count(i)/user[i]

    answer=[[v,i+1] for i,v in enumerate(user[1:])]
    
    for idx in range(N-1):
        for j in range(idx+1,N):
            if answer[idx][0] < answer[j][0]: answer[idx],answer[j]=answer[j],answer[idx]
            elif answer[idx][0]==answer[j][0] and answer[idx][1]>answer[j][1]: answer[idx],answer[j]=answer[j],answer[idx]

    return [value[1] for value in answer]