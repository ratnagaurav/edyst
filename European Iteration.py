n=int(input())
rom=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
def check(n):
    if 1<=n<=3999:
        return True
    else:
        return False
    
def roman(n):
    ans=""
    global rom
    for i in range(len(rom)):
        rem=n%rom[i][1]
        val=n//rom[i][1]
        ans+=val*rom[i][0]
        n=rem
    return ans
baseval={'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
while True:
    if not check(n):
        break
    r=roman(n)
    mxval=0
    for i in r:
        if baseval[i]>mxval:
            mxval=baseval[i]
    b=mxval+1
    
    s=0
    k=len(r)-1
    for i in r:
        s+=baseval[i]*(b**k)
        k-=1
    n=s
print(n)
    
