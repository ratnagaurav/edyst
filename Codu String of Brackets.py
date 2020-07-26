arr=input()
stack=[]
opening=['[','{','(']
closing=[']','}',')']
c=0
imp=False
temp=0
for i in arr:
    if i in opening:
        stack.append(i)
        count=0
        temp+=1
    elif i==']':
        if stack[-1]=='[':
            stack.pop()
            if count>=2:
                c+=temp
                temp=0
            else:
                imp=True
                temp=0
        else:
            imp=True
    elif i=='}':
        if stack[-1]=='{':
            stack.pop()
            if count>=2:
                c+=temp
                temp=0
            else:
                imp=True
                temp=0
        else:
            imp=True
    elif i==')':
        if stack[-1]=='(':
            stack.pop()
            if count>=2:
                c+=temp
                temp=0
            else:
                imp=True
                temp=0
        else:
            imp=True
    elif i=='*':
        count+=1

if not imp:
    print("Yes",c)
else:
    print("No",c)
