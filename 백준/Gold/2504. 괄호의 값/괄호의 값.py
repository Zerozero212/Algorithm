s=input()
li=[]
total=0
tmp=1
for i in range(len(s)):
    if s[i] == "(":
        li.append(s[i])
        tmp*=2
    elif s[i] == "[":
        li.append(s[i])
        tmp*=3
    elif s[i] == ")":
        if not li or li[-1] == "[":
            total = 0
            break
        elif s[i-1] == "(":
            total+=tmp
        li.pop()
        tmp//=2
    else:
        if not li or li[-1] == "(":
            total=0
            break
        elif s[i-1] == "[":
            total+=tmp
        li.pop()
        tmp//=3

if li:
    print(0)
else:
    print(total)