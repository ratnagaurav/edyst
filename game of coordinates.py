from math import gcd
T=int(input())
for _ in range(T):
    x,y=[int(x) for x in input().split()]
    if gcd(x,y)==1:
        print("Yes")
    else:
        print("No")

