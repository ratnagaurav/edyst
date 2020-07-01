num=int(input())
arr=[int(x) for x in input().split()]
def primefac(n):
    c=0
    while n%2==0:
        c+=1
        n=n/2
    i=3
    while i*i<=n:
        while n%i==0:
            c+=1
            n=n/i
        i+=2
    if n>2:
        c+=1
    return c
count=[]
for i in arr:
    count.append(primefac(i))
d=0
for i in count:
    d= d^i
if d== 0:
    print("JASBIR")
else:
    print("AMAN")






'''l=[0]*10001
for i in range(3,10001,2):
    l[i]=1

#seive logic
for i in range(3,10001,2):
    if l[i]==1:
        for j in range(i*i,10001,i):
            l[j]=0

l[1]=l[0]=0
l[2]=1
prime=[]
for i in range(10001):
    if l[i]==1:
        prime.append(i)

num=int(input())
arr=[int(x) for x in input().split()]
count=[]
for n in arr:
    c=0
    temp=n
    for i in prime:
        if i>temp:
            break
        while n>1 and n%i==0:
            n=n//i
            c+=1
    count.append(c)
    '''