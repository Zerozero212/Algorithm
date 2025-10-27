def solution(id_list, report, k):
    answer = {name:0 for name in id_list}
    notion = {name : set() for name in id_list}
    
    for individual_report in report:
        user,target = individual_report.split()
        notion[target].add(user)
    
    for name in id_list:
        if len(notion[name])>=k:
            for user in notion[name]:
                answer[user]+=1
    
    return list(answer.values())