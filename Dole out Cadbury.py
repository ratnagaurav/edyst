T=int(input())
for _ in range(T):
    p,q,r,s=[int(x) for x in input().split()]
    c=0
    l=[]
    for i in range(p,q+1):
        for j in range(r,s+1):
            l.append([i,j])
    for i in l:
        n1=i[0]
        n2=i[1]
        while True:
            sq=min(n1,n2)
            if sq==0:
                break
            elif sq==1:
                c+=max(n1,n2)
                break
            else:
                if sq==n1:
                    r=n2//sq
                    n2=n2%sq
                    c+=r
                elif sq==n2:
                    r=n1//sq
                    n1=n1%sq
                    c+=r
    print(c)