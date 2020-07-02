n=int(input())
l=[1]*(n+1)
for i in range(3,n+1):
    l[i]=(l[i-3]+l[i-1])%1000000007
print(l[n])
#print(l)




