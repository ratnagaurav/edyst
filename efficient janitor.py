n=int(input())
arr=[float(x) for x in input().split()]
arr.sort()
c=0
l=0
for i in range(n-1,-1,-1):
    if arr[i]>1.99:
        c+=1
    elif arr[i]<=1.99:
        if arr[i]+arr[l]<=3:
            l+=1
        c+=1
    if l>=i:
        break
         
print(c)



