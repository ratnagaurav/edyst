T=int(input())
for _ in range(T):
    arr=[int(x) for x in input().split()]
    m=arr[0]
    n=arr[1]
    mat=[]
    c=0
    l=[]
    for i in range(2,len(arr)):
        if c==n:
            mat.append(l)
            c=0
            l=[]
        l.append(arr[i])
        c+=1
    mat.append(l)
    
    
    t=[[0 for _ in range(n)] for _ in range(m)]
    
    for col in range(n-1,-1,-1):
        for row in range(m):
            #right
            if col==n-1:
                right=0
            else:
                right=t[row][col+1]
            #right up
            if row==0 or col==n-1:
                right_up=0
            else:
                right_up=t[row-1][col+1]
            #right_down
            
            if row==m-1 or col==n-1:
                right_down=0
            else:
                right_down=t[row+1][col+1]
                
            t[row][col]=mat[row][col]+ max(right,right_up,right_down)
            
    mx=t[0][0]
    for i in range(m):
        mx=max(mx,t[i][0])
    print(mx)



###################################################

t=int(input())
for _ in range(t):
    a=[int(x) for x in input().split()]
    m=a[0]
    n=a[1]
    gold=[]
    c=2
    #filling the gold matrix from input
    for i in range(m):
        temp=[]
        for j in range(n):
            temp.append(a[c])
            c+=1
        gold.append(temp)            

    #make a matrix of m*n and initialize it from 0

    t=[[0 for i in range(n)]for j in range(m)]

    # now check the condition of right,right_up,right_down
    # fill the last col of  matrix
    # by takin the values same as the last col of gold matrix
    # samjh lena ratna gaurav

    for col in range(n-1,-1,-1):
        for row in range(m):

            #last col fill kro
            #last col se right nhi ja skte
            # right jaane ka condition likhenge
            if col == n-1 :
                right = 0

            else:
                right = t[row][col+1]

            #right_up ka condition likho,,hass kaahe rha hai :)....soacho kya hoga
            # 0th row se uper nhi jaayenge pel

            if row == 0 or col == n-1:
                right_up = 0
            else:
                right_up = t[row-1][col+1]  # kya soach rha hai be :):):)

            #comment se uska yaad aa rha hai kya :):):)
            #koi baat nhi re

            #chal av right_down ka code ka likho
            #avi tak uske baare mei soach rha hai hahahaha:):)

            if row == m-1 or col == n-1:
                right_down = 0
            else:
                right_down = t[row+1][col+1]

            # av dekho ki max kya hoga
            # are bsdk yahan dhyan do
            #av jayda maat muskrao

            t[row][col] = gold[row][col] + max(right,right_down,right_up)  
            # samjh mei aaya be# hm apne chori krke likh rhe hai

            #iss tarah se t matrix fill ho jaayega

    #jo v maximum ans hoga wo ist col mei aayega # so ans mill gya be
    res = t[0][0]
    for i in range(1,m):

        res = max(res,t[i][0])

    print(res)











                
                
