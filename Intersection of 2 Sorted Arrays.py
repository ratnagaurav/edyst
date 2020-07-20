T=int(input())
for _ in range(T):
    arr1=[int(x) for x in input().split()]
    arr2=[int(x) for x in input().split()]
    n1=arr1[0]
    n2=arr2[0]
    arr1=arr1[1:]
    arr2=arr2[1:]
    k=0
    for i in range(n1):
        for j in range(k,n2):
            if arr1[i]==arr2[j]:
                print(arr1[i],end=" ")
                k=j+1
            elif arr1[i]<arr2[j]:
                break
    print()
