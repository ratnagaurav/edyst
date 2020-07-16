T=int(input())
for _ in range(T):
    n,k=[int(x) for x in input().split()]
    A=[int(x) for x in input().split()]
    B=[int(x) for x in input().split()]
    num=2*k
    s=0
    for i in range(n):
        s+=A[i]*B[i]
    new=s
    for i in range(n):
        temp=A[i]*B[i]
        tempinc=(A[i]+num)*B[i]
        tempdec=(A[i]-num)*B[i]
        val=(s-temp)+min(tempinc,tempdec)
        if val<new:
            new=val
    print(new)
