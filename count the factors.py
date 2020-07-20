try:
    n=int(input())
    factors=[]
    def primefac(n):
        global factors
        while n%2==0:
            factors.append(2)
            n=n//2

        i=3
        while i*i<=n:
            while n%i==0:
                factors.append(i)
                n=n//i
            i+=2
        if n>2:
            factors.append(n)

    for i in range(2,n+1):
        primefac(i)
    factors.sort()
    count=[]
    c=1
    for i in range(len(factors)-1):
        if factors[i+1]==factors[i]:
            c+=1
        else:
            print(c,end=" ")
            c=1
    print(c)
except:
    print("Invalid Input")