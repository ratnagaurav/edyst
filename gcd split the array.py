from math import gcd
T=int(input())
for _ in range(T):
    n=int(input())
    arr=[int(x) for x in input().split()]
    l=[0]*(n+1)
    for i in range(n-1,-1,-1):
        l[i]=1+l[i+1]
        for j in range(i+1,n):
            if gcd(arr[i],arr[j])>1:
                l[i]=min(l[i],1+l[j+1])
    print(l[0])




