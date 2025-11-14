ans = dict()
for ch in input():
    CH = ch.upper()
    if CH in ans: ans[CH]+=1
    else: ans[CH]=1

li = [(v,k) for k,v in ans.items()]
li.sort()

if len(li)>1:
    if li[-1][0] == li[-2][0]: print('?')
    else: print(li[-1][1])
else: print(li[-1][1])