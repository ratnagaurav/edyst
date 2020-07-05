T=int(input())
for _ in range(T):
    F,B,t,D=[int(x) for x in input().split()]
    f=F*t #time taken forward
    b=B*t #time taken for backward
    s=0
    while D>0:
        if D<=B: #residue
            s+=D*t
            break
        D=D-B
        s+=b
        D=D+F
        s+=f
    print(s)
    


