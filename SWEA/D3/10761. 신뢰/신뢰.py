T=int(input())
for tc in range(1,T+1):
    arr=input().split()

    o_time=b_time=total_time=0
    o_pos=b_pos=1
    turn=0  # orange: 1 / blue: 2

    for i in range(1,int(arr[0])*2+1,2):
        if arr[i]=='O': # o->o
            new_o_pos=int(arr[i+1])
            if turn!=2:
                total_time += abs(new_o_pos-o_pos)+1
                o_time=total_time  # o가 끝났을 때 시간 저장
                o_pos=new_o_pos
            else:  # b->o
                if o_time+abs(new_o_pos-o_pos)<=total_time: #B가 움직이는 동안 O가 움직임
                    total_time+=1
                else:
                    total_time = o_time+abs(new_o_pos-o_pos) + 1
                o_time=total_time  
                o_pos=new_o_pos
            turn=1

        else:
            new_b_pos=int(arr[i+1])
            if turn!=1:
                total_time += abs(new_b_pos-b_pos)+1
                b_time=total_time  # o가 끝났을 때 시간 저장
                b_pos=new_b_pos
            else:  # b->o
                if b_time+abs(new_b_pos-b_pos)<=total_time: #B가 움직이는 동안 O가 움직임
                    total_time+=1
                else:
                    total_time = b_time+abs(new_b_pos-b_pos) + 1
                b_time=total_time  
                b_pos=new_b_pos
            turn=2
    
    print(f'#{tc} {total_time}')