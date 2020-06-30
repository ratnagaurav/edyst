import sys
T=int(input())
def sq(x,y):
    return (x**2+y**2)**(0.5)
for _ in range(T):
    x=float(input())
    y=float(input())
    va=float(input())
    vb=float(input())
    val=int(min(x/va,y/vb))
    min_dist=sys.maxsize
    while (x>=0 or y>=0):
        val=sq(x,y)
        if val<min_dist:
            min_dist=val
        x=x-va
        y=y-vb
    if min_dist==0:
        print("0.0")
    else:
        print('{:.4f}'.format(min_dist))


