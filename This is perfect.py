T=int(input())
for _ in range(T):
    n=int(input())
    if n==1:
        print("NO")
        continue
    fact=[1]
    i=2
    while i*i<=n:
        if n%i==0:
            fact.append(i)
            fact.append(n//i)
        i+=1
    if sum(fact)==n:
        print("YES")
    else:
        print("NO")

