T=int(input())
for _ in range(T):
    arr=[int(x) for x in input().split()]
    n=arr[0]
    arr=arr[1::]
    s=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<=arr[i]:
                s+=arr[i]-arr[j]
                break
        else:
            s+=arr[i]
    print(s)



