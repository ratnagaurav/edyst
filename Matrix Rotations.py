n=int(input().strip())
original=[]
total=0
for i in range(n):
    original.append([int(x) for x in input().strip().split()])
matrix=list(map(list,original))
def rotate(arr):
    global n
    count=(n)//2
    for i in range(count):
        for j in range(i,n-i-1):
            temp=arr[i][j]
            arr[i][j]=arr[n-1-j][i]
            arr[n-1-j][i]=arr[n-1-i][n-1-j]
            arr[n-1-i][n-1-j]=arr[j][n-1-i]
            arr[j][n-1-i]=temp

while True:
    cmd=input().split()
    if cmd[0]=='A':
        angle=int(cmd[1])//90
        for r in range(angle%4):
            rotate(matrix)
        total+=angle%4
    elif cmd[0]=='Q':
        print(matrix[int(cmd[1])-1][int(cmd[2])-1])
    elif cmd[0]=='U':
        original[int(cmd[1])-1][int(cmd[2])-1]=int(cmd[3])
        matrix=list(map(list,original))
        for r in range(total%4):
            rotate(matrix)
    elif cmd[0]=='-1':
        break
