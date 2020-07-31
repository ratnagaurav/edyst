slabs=[int(x) for x in input().split()]
per=[int(x) for x in input().split()]
rebate=int(input())
taxpaid=[int(x) for x in input().split()]

def empsal(txpaid,slabs,per,n):
    sal=slabs[0]
    for i in range(n-1):
        if txpaid==0:
            return sal
        diff=slabs[i+1]-slabs[i]
        tax=diff*per[i]/100
        if tax>txpaid:
            val=(txpaid*100)/per[i]
            return int(sal+val)
        txpaid-=tax
        sal+=diff
    val=(txpaid*100)/per[n-1]
    return int(sal+val)
       
n=len(slabs)

totalsal=0
for i in taxpaid:
    totalsal+=empsal(i,slabs,per,n)+rebate
print(totalsal)
