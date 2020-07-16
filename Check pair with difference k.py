T=int(input())
for _ in range(T):
    arr=[int(x) for x in input().split()]
    k=int(input())
    n=arr[0]
    arr=arr[1:]
    flag=0
    i=0
    j=1
    while i<n and j<n:
        diff=arr[j]-arr[i]
        if diff==k and i!=j:
            flag=1
            break
        elif diff<k:
            j=j+1
        else:
            i=i+1
    print(flag)