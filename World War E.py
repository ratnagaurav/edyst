from math import factorial
from fractions import Fraction
T=int(input())
def ncr(n,r):
    if n==r:
        return 1
    else:
        num=factorial(n)
        den=factorial(r)*factorial(n-r)
    return num/den
def mul(f,k):
    ans=Fraction(1,1)
    for _ in range(k):
        ans*=Fraction(f)
    return ans
for _ in range(T):
    normal,H,L1,L2,M,C=[int(x) for x in input().split()]
    pns=abs(L1-L2)
    special=normal+C
    specsum=special*M
    norsum=normal*M
    s=0
    if specsum<H:
        print("RIP")
        continue
    for i in range(M+1):
        if norsum+(i*C)>H:
            s=i
            break
    total=0     
    for i in range(s,M+1):
        f1=mul(Fraction(L1,L2),i)
        f2=mul(Fraction(pns,L2),M-i)
        total+=Fraction(ncr(M,i))*Fraction(f1)*Fraction(f2)
    
    print(Fraction(total))

    
