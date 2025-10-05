def solution(today, terms, privacies):
    answer = []
    today=list(map(int,today.split('.')))
    valid_duration = dict()
    for term in terms:
        opt,duration = term.split()
        valid_duration[opt]=int(duration)
        
    for i in range(len(privacies)):
        date,opt=privacies[i].split()
        date=list(map(int,date.split('.')))
        date[1]+=valid_duration[opt]
        if date[1] > 12:
            tmp = (date[1] - 1) // 12    
            date[0] += tmp
            date[1] -= 12 * tmp
        
        if date[2]==1:
            if date[1]==1:
                date[0]-=1
                date[1]=12
                date[2]=28
            else:
                date[1]-=1
                date[2]=28
        else: date[2]-=1
        
        if date[0]<today[0] or (date[0]==today[0] and date[1]<today[1]) or (date[0]==today[0] and date[1]==today[1] and date[2]<today[2]):
            answer.append(i+1)
    return sorted(answer)