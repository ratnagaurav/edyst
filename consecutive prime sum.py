T=int(input())
l=[0]*1000000
for i in range(3,1000000,2):
	l[i]=1

#seive logic
for i in range(3,1000000,2):
	if l[i]==1:
		for j in range(i*i,1000000,i):
			l[j]=0

l[1]=l[0]=0
l[2]=1
c=0

for _ in range(T):
    n=int(input())
    primes=[]
    c=0
    primecount=0
    for i in range(n+1):
        if l[i]==1:
            primes.append(i)
            c+=1
    for i in range(2,c):
        s=0
        for j in range(i):
            s+=primes[j]
            if s==primes[i]:
                primecount+=1
            elif s>primes[i]:
                break
    print(primecount)



