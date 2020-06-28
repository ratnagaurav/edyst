prime=[2,3,5,7,11,13,17,19,23,29,31]
T=int(input())
for _ in range(T):
    c=0
    L,R=[int(x) for x in input().split()]
    for i in range(L,R+1):
        for j in prime:
            if 1<<(j-1) & i:
                c+=1
    print(c)
