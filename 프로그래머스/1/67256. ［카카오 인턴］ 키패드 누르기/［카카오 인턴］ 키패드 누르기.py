def solution(numbers, hand):
    ans=[]
    key_list={
              1:[0,0],2:[0,1],3:[0,2],
              4:[1,0],5:[1,1],6:[1,2],
              7:[2,0],8:[2,1],9:[2,2],
              '*':[3,0],0:[3,1],'#':[3,2],
             }
    left=key_list['*']
    right=key_list['#']
    
    for num in numbers:
        if num in set((1,4,7)): 
            ans.append('L')
            left=key_list[num]
        elif num in set((3,6,9)): 
            ans.append('R')
            right=key_list[num]
        else:
            tmp=key_list[num]
            left_dist=abs(left[0]-tmp[0])+abs(left[1]-tmp[1])
            right_dist=abs(right[0]-tmp[0])+abs(right[1]-tmp[1])
            if left_dist<right_dist:
                ans.append('L')
                left=tmp
            elif left_dist>right_dist:
                ans.append('R')
                right=tmp
            else:
                if hand=="left": 
                    ans.append('L')
                    left=tmp
                else: 
                    ans.append('R')
                    right=tmp
    
    return ''.join(ans)