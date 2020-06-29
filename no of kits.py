n=int(input())
arr=[int(x) for x in input().split()]
s=0
c=0
arr.sort(reverse=True)
i=0
while s<=sum(arr)//2:
    s+=arr[i]
    c+=1
    i+=1
print(c)



