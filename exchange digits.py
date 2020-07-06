from itertools import permutations
a,b=[int(x) for x in input().split()]
a=list(str(a))
val=[''.join(p) for p in permutations(a)]
val.sort()
for i in range(len(val)):
    if int(val[i])>b and val[i][0]!='0':
        print(int(val[i]))
        break
else:
    print(-1)



