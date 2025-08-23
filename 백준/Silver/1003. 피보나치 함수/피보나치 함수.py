def f(n):
    if n==0: return (1,0)
    elif n==1: return (0,1)
    o_x,o_y=1,0
    t_x,t_y=0,1

    for _ in range(n-2):
        o_x,o_y=o_y,o_x+o_y
        t_x,t_y=t_y,t_x+t_y
    return (o_x+t_x,o_y+t_y)

T=int(input())
for t in range(1,T+1):
    N=int(input())
    print(*f(N))