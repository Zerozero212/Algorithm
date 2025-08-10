T = int(input())
for tc in range(1,T+1):
    N,Q = map(int,input().split())
    box = [0]*(N+1) #입력할 상자 생성
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for I in range(L,R+1):
            box[I] = i #해당 번호 박스에 바로 할당
    print(f'#{tc}',*box[1:])
