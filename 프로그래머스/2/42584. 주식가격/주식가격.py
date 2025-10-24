def solution(prices):
    answer = []
    time=[0]*len(prices)
    t=1
    end_time=len(prices)
    for i in range(len(prices)):
        if not answer: answer.append((i,prices[i],t))
        else:
            while answer:
                idx,price,nt = answer.pop()
                if price <= prices[i]:
                    answer.extend([(idx,price,nt),(i,prices[i],t)])
                    break
                else:
                    time[idx] = t-nt
            
            if not answer:
                answer.append((i,prices[i],t))
        
        t+=1
    
    while answer:
        idx,_,nt = answer.pop()
        time[idx] = end_time-nt
        
    return time