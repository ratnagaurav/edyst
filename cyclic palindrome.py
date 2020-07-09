T=int(input())
def ispalin(s):
    if len(s)==0 or len(s)==1:
        return True
    if s[0]==s[-1]:
        return ispalin(s[1:-1])
    else:
        return False
for _ in range(T):
    s=list(input())
    t=s[::]
    n=len(s)
    cs=0
    ct=0
    if ispalin(s):
        print(cs)
    else:
        for i in range(n):
            #left rotation
            temp=s.pop(0)
            s.append(temp)
            #right rotation
            tmp=t.pop()
            t.insert(0,tmp)
            cs+=1
            ct+=1
            if ispalin(s) or ispalin(t):
                print(min(cs,ct))
                break
        else:
            print(-1)