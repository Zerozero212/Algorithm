N=int(input())
for _ in range(N):
    s=input()
    cnt=0
    is_palindrome=0
    l,r=0,len(s)-1
    while True:
        cnt+=1
        if l>=r:
            is_palindrome=1
            break
        elif s[l]!=s[r]:break
        l+=1
        r-=1
    
    print(is_palindrome,cnt)