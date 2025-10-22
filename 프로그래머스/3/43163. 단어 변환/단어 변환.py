def solution(begin, target, words):
    if target not in words: return 0
    N=len(words)
    v=[0]*N
    cnt=1e9
    
    def dfs(ch,k):
        nonlocal cnt
        if cnt<=k: return
        if ch==target:
            cnt=k
            return
        
        def comp(ch1,ch2):
            cnt=0
            for i in range(len(ch1)):
                if ch1[i]!=ch2[i]: cnt+=1
            if cnt==1: return 1
            else: return 0
            
        for i in range(N):
            if v[i]: continue
            if comp(ch,words[i]):
                v[i]=1
                dfs(words[i],k+1)
                v[i]=0
    dfs(begin,0)
    
    return cnt if cnt!=1e9 else 0