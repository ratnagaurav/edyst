n=int(input())
bride=input()
groom=input()
rum=0
mojito=0
for i in range(n):
	if groom[i]=='r':
		rum+=1
	else:
		mojito+=1
val=0
for i in range(n):
	if bride[i]=='r':
		if rum>0:
			rum-=1
		else:
			val=i
			break
	else:
		if mojito>0:
			mojito-=1
		else:
			val=i
			break
if val==0:
    print(val)
else:
    print(n-val)