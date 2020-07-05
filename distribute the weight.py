T=int(input())
def possible(arr,m,k):
    currsub=arr[0]
    subs=1
    flag=True
    for i in range(1,len(arr)):
        if arr[i]+currsub>k:
            currsub=arr[i]
            subs+=1
        else:
            currsub+=arr[i]
        if subs>m:
            flag=False
            break
    return flag
for _ in range(T):
    n,m=[int(x) for x in input().split()]
    arr=[int(x) for x in input().split()]
    left=max(arr)
    right=sum(arr)
    mid=(left+right)//2
    val=[]
    while left<=right:
        if possible(arr,m,mid):
            val.append(mid)
            right=mid-1
        else:
            left=mid+1
        mid=(left+right)//2
    print(min(val))
        




