T=int(input())
for _ in range(T):
    n=int(input())
    arr=[int(x) for x in input().split()]
    idx=0
    c=0
    high=0
    for i in range(n-1):
        if arr[i+1]>=arr[i]:
            c+=1
        else:
            if c>high:
                high=c
                idx=i-c
            c=0
    if c>high:
        high=c
        idx=i+1-c
    for i in range(idx,idx+high+1):
        print(arr[i],end=" ")
    print()


