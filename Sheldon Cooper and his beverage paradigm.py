n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
x=int(input())
arr.sort()
def solve(arr,i,n,x):
    low=i
    high=n
    while low<high:
        if arr[low]+arr[high]==x:
            return True
        elif arr[low]+arr[high]>x:
            high-=1
        else:
            low+=1
    return False
for i in range(n-2):
    if solve(arr,i+1,n-1,x-arr[i]):
        print(True)
        break
else:
    print(False)