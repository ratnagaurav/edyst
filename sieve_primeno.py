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
for i in range(334):
	if l[i]==1:
		print(i,end=",")
		c+=1

