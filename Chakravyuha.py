n=int(input())
mat=[[0 for x in range(n)] for y in range(n)]
num=1
low=0
high=n-1
p=1
def powerpoint(n):
    if n%11==0:
        return True
    return False
count=(n+1)//2
cor=[(0,0)]
for i in range(count):
    for j in range(low,high+1):
        mat[i][j]=num
        if powerpoint(num):
            p+=1
            cor.append((i,j))
        num+=1
    for j in range(low+1,high+1):
        mat[j][high]=num
        if powerpoint(num):
            p+=1
            cor.append((j,high))
        num+=1
    for j in range(high-1,low-1,-1):
        mat[high][j]=num
        if powerpoint(num):
            p+=1
            cor.append((high,j))
        num+=1
    for j in range(high-1,low,-1):
        mat[j][low]=num
        if powerpoint(num):
            p+=1
            cor.append((j,low))
        num+=1
    low+=1
    high-=1
for i in range(n):
    for j in range(n):
        print(mat[i][j],end="\t")
    print()
print(f"Total Power points : {p}")
for i in cor:
    print(f"({i[0]},{i[1]})")

