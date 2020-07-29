rr1=float(input())
player=[int(x) for x in input().split()]
delivery=input().split()
d=len(delivery)
rr2=float(input())
runs=0
for i in delivery:
    if i!='W':
        runs+=int(i)

num=abs((d*rr2)/6-runs)
den=abs(rr1-rr2)/6
balls=round(num/den)
start=0
left=balls%6
if left==0:
    pass
else:
    start=6-left
    for i in range(start):
        if delivery[i]=='W':
            player[0]=0
        else:
            if delivery[i] == '1' or delivery[i] == '3' or delivery[i] == '5':
                player[0]+=int(delivery[i])
                player=player[::-1]
            elif delivery[i] == '2' or delivery[i] == '4' or delivery[i] == '6':
                player[0]+=int(delivery[i])
    player=player[::-1]
c=0    
for i in range(start,d):
    if c==6:
        c=0
        player=player[::-1]
    if delivery[i]=='W':
        player[0]=0
    else:
        if delivery[i] == '1' or delivery[i] == '3' or delivery[i] == '5':
            player[0]+=int(delivery[i])
            player=player[::-1]
        elif delivery[i] == '2' or delivery[i] == '4' or delivery[i] == '6':
            player[0]+=int(delivery[i])
    c+=1
if c%6==0:
    player=player[::-1]
    
total=rr1*(balls/6)+runs
print(round(total),player[0],player[1])