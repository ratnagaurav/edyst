nums=[int(x) for x in input().split()]



n=len(nums)
s=sum(nums)
t=[[False]*(s//2+1)]
for i in range(1,n+1):
    t.append([True])
t[0][0]=True
for i in range(1,n+1):
    for j in range(1,s//2+1):
        if nums[i-1]<=j:
            t[i].append(t[i-1][j-nums[i-1]] or t[i-1][j])
        else:
            t[i].append(t[i-1][j])
val=0
d=[]
for i in range(s//2+1):
	if t[n][i]==True:
		d.append(i)
print(max(d[-1],s-d[-1]))