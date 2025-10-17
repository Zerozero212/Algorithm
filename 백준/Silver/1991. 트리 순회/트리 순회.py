def pre_order(ch):
    if ch=='None': return

    print(ch,end='')
    pre_order(alphabet[ch][0])
    pre_order(alphabet[ch][1])

def in_order(ch):
    if ch=='None': return

    in_order(alphabet[ch][0])
    print(ch,end='')
    in_order(alphabet[ch][1])

def post_order(ch):
    if ch=='None': return

    post_order(alphabet[ch][0])
    post_order(alphabet[ch][1])
    print(ch,end='')

N=int(input())
alphabet = dict()

for _ in range(N):
    p,c1,c2 = input().split()
    tmp = []
    for c in (c1,c2):
        if c!='.':
            tmp.append(c)
        else:
            tmp.append('None')
    alphabet[p]=tmp

pre_order('A')
print()
in_order('A')
print()
post_order('A')