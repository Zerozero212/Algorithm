N=int(input())
negative = []
positive = []
one = []

for _ in  range(N):
    num = int(input())
    if num>1: positive.append(num)
    elif num==1: one.append(num)
    else: negative.append(num)

negative.sort()
positive.sort(reverse=True)

ans=0

negative_last=0
len_negative = len(negative)

if len_negative%2:
    negative_last = negative[-1]
    len_negative-=1

if len_negative>1:
    for i in range(0,len_negative,2):
        ans += negative[i]*negative[i+1]
ans+=negative_last

positive_last=0
len_positive = len(positive)

if len_positive%2:
    positive_last = positive[-1]
    len_positive-=1

if len_positive>1:
    for i in range(0,len_positive,2):
        ans += positive[i]*positive[i+1]
ans+=positive_last

ans += sum(one)

print(ans)