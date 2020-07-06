##############################          improved approach           ###########################
totalroom=int(input())
r1,r2=[float(x) for x in input().split()]
target=float(input())

patients={}
for i in range(53):
    patients[i]=0
for i in range(1,13):
    if i==2:
        loop=28
    elif i in (1,3,5,7,8,10,12):
        loop=31
    else:
        loop=30
    for j in range(1,loop+1):
        oneday=((6-i)**2)+abs(j-15)
        patients[oneday]+=1
def revenue(patients,totalroom,tvroom):
    rev=0
    nontv=totalroom-tvroom
    for i in patients:
        if i<=nontv:
            rev+=r2*i*patients[i]
        elif nontv<i<=totalroom:
            rem=i-nontv
            rev+=((nontv*r2)+(rem*r1))*patients[i]
        elif i>totalroom:
            rev+=((nontv*r2)+(tvroom*r1))*patients[i]
    return rev

            
left=0
right=totalroom
mid=(left+right)//2
m=totalroom
while left<=right:
    achieve=revenue(patients,totalroom,mid)
    if achieve<target:
        left=mid+1
    elif achieve>target:
        right=mid-1
        if mid<m:
            m=mid
    mid=(left+right)//2
print(m)




##############################          normal approach           ###########################
totalroom=int(input())
r1,r2=[float(x) for x in input().split()]
target=float(input())

patients={}
for i in range(53):
    patients[i]=0
for i in range(1,13):
    if i==2:
        loop=28
    elif i in (1,3,5,7,8,10,12):
        loop=31
    else:
        loop=30
    for j in range(1,loop+1):
        oneday=((6-i)**2)+abs(j-15)
        patients[oneday]+=1
def revenue(patients,totalroom,tvroom):
    rev=0
    nontv=totalroom-tvroom
    for i in patients:
        if i<=nontv:
            rev+=r2*i*patients[i]
        elif nontv<i<=totalroom:
            rem=i-nontv
            rev+=((nontv*r2)+(rem*r1))*patients[i]
        elif i>totalroom:
            rev+=((nontv*r2)+(tvroom*r1))*patients[i]
    return rev
for i in range(totalroom+1):
    achieve=revenue(patients,totalroom,i)
    if achieve>=target:
        print(i)
        break
else:
    print(totalroom)
            
    


