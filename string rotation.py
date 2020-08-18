s=input().strip()
l=len(s)
final=""
q=int(input())
ind=0
def count(arr):
    d={}
    for i in arr:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
def countequal(a,b):
    for i in a:
        if i not in b or a[i]!=b[i]:
            return False
    return True
def isAnagram(s,final):
    if len(s)<len(final):
        return False
    countfinal=count(final)
    for i in range(0,len(s)-len(final)+1):
        window=s[i:i+len(final)]
        charw=count(window)
        
        if countequal(charw,countfinal):
            return True
    return False

for _ in range(q):
    d,n=input().strip().split()
    n=int(n)
    if d=='L':
        ind=(ind+n) % l
    else:
        ind=(ind-n) % l
    final+=s[ind]
if isAnagram(s,final):
    print("YES")
else:
    print("NO")







#sb test case pass nhi kiya tha


from itertools import permutations
s=input().strip()
l=len(s)
temp=s[:]
final=""
q=int(input())

for _ in range(q):
    d,n=input().strip().split()
    n=int(n)%l
    if n==l:
        continue
    elif d=='L':
        s=s[n::]+s[0:n]
        final+=s[0]
    elif d=="R":
        s=s[-n::]+s[0:len(s)-n]
        final+=s[0]
f=0
for i in list(permutations(final)):
    if ''.join(i) in temp:
        print("YES")
        break
    
else:
    print("NO")
