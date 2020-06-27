T=int(input())
def isprogram(s):
    if s[0]=='{' and s[-1]=='}':
        return True
    else:
        return False
def ismain(s):
    c1=0
    c2=0
    arr=[]
    for i in range(len(s)):
        if s[i]=='<':
            c1+=1
            arr.append(i)
        if s[i]=='>':
            c2+=1
            arr.append(i)
    if c1==c2==1 and arr[0]<arr[1]:
        return arr
    return False
def insidemain(s):
    stack=[]
    for i in s:
        if i=='(' or i==')':
            return False
        elif i=='{':
            stack.append(i)
        elif i=='}':
            try:
                if stack[-1]=='{':
                    stack.pop()
            except:
                return False
    if stack==[]:
        return True
    return False
def loop(s):
    c=0
    alpha=0
    arr=[]
    stack=[]
    for i in s:
        if i=='(':
            c+=1
            arr.append(i)
        elif i==')':
            c-=1
            try:
                if arr[-1]=='(':
                    arr.pop()
                    if alpha>100:
                        return False
                    alpha=0
            except:
                return False
        elif i=='P' and c==1:
            alpha+=1
        if i=='{':
            if c==1:
                stack.append(i)
            else:
                return False
        elif i=="}":
            if c==1:
                try:
                    if stack[-1]=='{':
                        stack.pop()
                except:
                    return False
            else:
                return False
        if c<0 or c>1:
            return False
    if stack!=[] or arr!=[]:
        return False
    return True
for _ in range(T):
    aaa=input().split()
    s=list("".join(aaa))
    if isprogram(s)==False:
        print("Compilation Errors")
        continue
    val=ismain(s)
    if val==False:
        print("Compilation Errors")
        continue
    
    if insidemain(s[val[0]+1:val[1]])==False:
        print("Compilation Errors")
        continue
        
    if loop(s[1:val[0]])==False or loop(s[val[1]+1:-1])==False:
        print("Compilation Errors")
        continue
    print("No Compilation Errors")

