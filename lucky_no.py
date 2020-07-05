T=int(input())
for _ in range(T):
    L,R=[int(x) for x in input().split()]
    c=0
    for n in range(L,R+1):
        i=2
        f=0
        while i*i<=n:
            if n%(i*i)==0:
                f=1
                break
            i+=1
        if f==0:
            c+=1
    print(c)



