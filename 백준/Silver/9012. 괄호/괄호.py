def is_valid(indi):
    tmp = []
    for ch in indi:
        if ch == '(':
            tmp.append(ch)
        else:
            if not tmp: return 0
            if tmp[-1] == ')': tmp.append(ch)
            else: tmp.pop()
    
    if tmp: return 0
    else: return 1

T = int(input())
ps_list = [list(input()) for _ in range(T)]
ans=[]

for indi_list in ps_list:
    if is_valid(indi_list): ans.append("YES")
    else: ans.append("NO")

for x in ans:
    print(x)