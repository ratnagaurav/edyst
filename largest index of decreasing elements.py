T=int(input())
for _ in range(T):
    arr=[int(x) for x in input().split()]
    n=arr[0]
    arr=arr[1::]
    c=0
    mx=0
    for i in range(n-1):
        if arr[i+1]<arr[i]:
            c+=1
            if i==n-2:
                mx=max(mx,c)
        else:
            mx=max(mx,c)
            c=0
    print(mx)