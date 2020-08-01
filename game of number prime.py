try:
    x=int(input())
    y=int(input())
    n=int(input())
    if x<0 or y<0 or x>y:
        raise ValueError
    def isNum(n):
        while True:
            num=n
            s=0
            while num!=0:
                r=num%10
                s+=r**2
                num=num//10
            n=s
            if s==58: #to find where to stop
                return False
            elif s==1:
                return True
    def prime(n):
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True
    c=0
    val=0
    for i in range(x,y+1):
        if i==1: #1 is not a prime
            continue
        if prime(i):
            if isNum(i):
                c+=1
            if c==n:
                val=i
                break
            
    if n==c:
        print(val)
    else:
        print("No number is present at this index")
except ValueError:
    print("Invalid Input")



