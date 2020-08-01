T=int(input())
baseval={'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

alpha=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def prime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
def changebase(num,b):
    global alpha
    ans=""
    while num!=0:
        rem=num%b
        ans+=alpha[rem]
        num=num//b
    return ans[::-1]
    
for _ in range(T):
    n,s=input().split()
    Nbase=0
    for i in n:
        if baseval[i]>Nbase:
            Nbase=baseval[i]
    Nbase+=1
    num=0
    p=len(n)-1
    for i in n:
        num+=baseval[i]*(Nbase**p)
        p-=1
    
    s1b=baseval[str(s)]+1
   
    while True:
        if prime(num):
            x=changebase(num,s1b)
            if s in x:
                print(x)
                break
        num+=1
