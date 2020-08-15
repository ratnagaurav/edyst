n=int(input())
sec=int(input())
part=[]
for i in range(n):
    arr=[int(x) for x in input().split()]
    part.append(arr)
lead=[0]*n
score=[0]*n
def leadcount(score,n):
    global lead
    mx=max(score)
    for k in range(n):
        if score[k]==mx:
            lead[k]+=1

for i in range(0,sec,2):
    for j in range(n):
        dist=part[j][-1]
        val=(part[j][i]*dist)+(part[j][i+1]*dist)
        score[j]+=val
    leadcount(score,n)
d=0
idx=0
for i in range(n):
    if lead[i]>d:
        d=lead[i]
        idx=i+1
print(idx)
