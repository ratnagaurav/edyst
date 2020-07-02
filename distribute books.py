n=int(input())
f=[0]*(n+1)
f[0]=0
f[1]=0
f[2]=1
for i in range(3,n+1):
    val=(i-1)*(f[i-1]+f[i-2])
    f[i]=(val%1000000007)
print(f[-1])