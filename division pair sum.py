T=int(input())
for _ in range(T):
    arr=[int(x) for x in input().split()]
    n=arr[0]
    arr=arr[1::]
    m=int(input())
    remainders={}
    for i in arr:
        curr=i%m
        if curr in remainders:
            remainders[curr]+=1
        else:
            remainders[curr]=1
    pair_sum=0
    for i in remainders:
        compl=m-i
        pairs=0
        if compl==m or (2*compl==m):
            pairs=remainders[i]*(remainders[i]-1)//2
        elif compl in remainders:
            pairs=remainders[i]*remainders[compl]
            remainders[i]=0
        pair_sum+=pairs
    print(pair_sum)


