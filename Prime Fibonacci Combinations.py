T=int(input())
def prime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def fibbo(a,b,n):
    f=[a,b]
    while n-2>0:
        f.append(f[-1]+f[-2])
        n-=1
    return f[-1]

for _ in range(T):
    n1,n2=[int(x) for x in input().split()]
    first_prime=[]
    for i in range(n1,n2+1):
        if prime(i):
            first_prime.append(str(i))
    n=len(first_prime)
    sec_prime=set()
    for i in range(n):
        for j in range(n):
            if i!=j:
                temp=int(first_prime[i]+first_prime[j])
                if prime(temp):
                    sec_prime.add(temp)
    sec=list(sec_prime)
    num=len(sec)
    mx=sec[0]
    mn=sec[0]
    for i in sec:
        if i>mx:
            mx=i
        if i<mn:
            mn=i
    print(fibbo(mn,mx,num))
