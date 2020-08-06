T=int(input())
for _ in range(T):
    n=int(input())
    arr=input().split()
    bits=[]
    for i in arr:
        num=str((11*int(max(i)))+(7*int(min(i))))
        bits.append(num[-2::])
    even=[0]*10
    odd=[0]*10
    for i in range(0,len(bits),2):
        odd[int(bits[i][0])]+=1
    for i in range(1,len(bits),2):
        even[int(bits[i][0])]+=1
    c=0
    s=0
    def pairs(n):
        if n<=1:
            return 0
        elif n==2:
            return 1
        elif n>2:
            return 2
    for i in range(10):
        s=pairs(even[i])+pairs(odd[i])
        if s>2:
            c+=2
        else:
            c+=s
    print(c)

