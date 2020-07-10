r,c=[int(x) for x in input().split()]
mat=[]
for i in range(r):
    mat.append([int(x) for x in input().split()])

dist=[]
quality=[]
def A(mat,i,j):
    if (i-1)<0 or (j-1)<0:
        return 0
    try:
        if mat[i-1][j-1]==1:
            return 1
        else:
            return 0
    except:
        return 0
def B(mat,i,j):
    if (i-1)<0:
        return 0
    try:
        if mat[i-1][j]==1:
            return 1
        else:
            return 0
    except:
        return 0
def C(mat,i,j):
    if (i-1)<0:
        return 0
    try:
        if mat[i-1][j+1]==1:
            return 1
        else:
            return 0
    except:
        return 0
def D(mat,i,j):
    if (j-1)<0:
        return 0
    try:
        if mat[i][j-1]==1:
            return 1
        else:
            return 0
    except:
        return 0
def E(mat,i,j):
    try:
        if mat[i][j+1]==1:
            return 1
        else:
            return 0
    except:
        return 0
def F(mat,i,j):
    if (j-1)<0:
        return 0
    try:
        if mat[i+1][j-1]==1:
            return 1
        else:
            return 0
    except:
        return 0
def G(mat,i,j):
    try:
        if mat[i+1][j]==1:
            return 1
        else:
            return 0
    except:
        return 0
def H(mat,i,j):
    try:
        if mat[i+1][j+1]==1:
            return 1
        else:
            return 0
    except:
        return 0
    
for i in range(r):
    for j in range(c):
        if mat[i][j]==1 and i==j==0:
            continue
        elif mat[i][j]==1:
            if i==0 and j==1:
                quality.append([sum([G(mat,i,j),F(mat,i,j),E(mat,i,j),H(mat,i,j)])])
            elif i==1 and j==0:
                quality.append([sum([C(mat,i,j),E(mat,i,j),G(mat,i,j),H(mat,i,j)])])
            elif i==1 and j==1:
                quality.append([sum([B(mat,i,j),C(mat,i,j),D(mat,i,j),E(mat,i,j),F(mat,i,j),G(mat,i,j),H(mat,i,j)])])
            else:
                quality.append([sum([A(mat,i,j),B(mat,i,j),C(mat,i,j),D(mat,i,j),E(mat,i,j),F(mat,i,j),G(mat,i,j),H(mat,i,j)])])
            
            
            
            quality[-1].append((i+1,j+1))


quality.sort(reverse=True)
val=quality[0][0]
loc=quality[0][1]
ssss=int((quality[0][1][0]**2 + quality[0][1][1]**2)**(0.5))
count=0
for i in range(len(quality)-1):
    if quality[i+1][0]<quality[i][0]:
        break
    elif quality[i+1][0]==quality[i][0]:
        cal1=int((quality[i+1][1][0]**2 + quality[i+1][1][1]**2)**(0.5))
        cal2=int((quality[i][1][0]**2 + quality[i][1][1]**2)**(0.5))
        if cal1<ssss:
            loc=quality[i+1][1]
            ssss=cal1
        elif cal1==cal2:
            count+=1
            break
            
if count!=0 and val>=1:
    print("Polygamy not allowed")
elif val==0:
    print("No suitable girl found")
else:
    print(f"{loc[0]}:{loc[1]}:{val}")

