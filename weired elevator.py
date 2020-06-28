import math
T=int(input())
def normalsieve(n):
    arr=[0]*(n+1)
    for i in range(3,n+1,2):
        arr[i]=1

    for i in range(3,n+1,2):
        if arr[i]==1:
            for j in range(i*i,n+1,i):
                arr[j]=0
    arr[1]=arr[0]=0
    arr[2]=1
    prime=[]
    for i in range(2,n+1):
        if arr[i]==1:
            prime.append(i)
    return prime
x_cases=[]
y_cases=[]
m_cases=[]
mx=1
for _ in range(T):
    x,y,m=[int(x) for x in input().split()]
    x_cases.append(x)
    y_cases.append(y)
    m_cases.append(m)
    mx=max(mx,x,y)
prime = normalsieve(mx)
for i in range(T):
    x,y,m=x_cases[i],y_cases[i],m_cases[i]
    if x==0 or y==0:
        print(-1)
        continue
    distance=0
    impossible=False
    hcf=math.gcd(x,y)
    x_dist=x//hcf
    y_dist=y//hcf
    for i in prime:
        if i>=m:
            impossible=True
            break
        while x_dist>1 and x_dist%i==0:
            x_dist=x_dist//i
            distance+=1
        if x_dist<=1:
            break
    if impossible:
        print(-1)
        continue
    for i in prime:
        if i>=m:
            impossible=True
            break
        while y_dist>1 and y_dist%i==0:
            y_dist=y_dist//i
            distance+=1
        if y_dist<=1:
            break
    if impossible:
        print(-1)
        continue
    print(distance,hcf)
