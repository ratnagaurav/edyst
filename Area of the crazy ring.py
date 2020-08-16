from math import pi
def collinear(x1, y1, x2, y2, x3, y3): 
    if ((y3 - y2)*(x2 - x1) == (y2 - y1)*(x3 - x2)): 
        return True 
    else: 
        return False
def side(x1,y1,x2,y2):
    val=((y2-y1)**2)+((x2-x1)**2)
    return val**(0.5)
T=int(input())
for _ in range(T//3):
    x1,y1=[float(x) for x in input().split()]
    x2,y2=[float(x) for x in input().split()]
    x3,y3=[float(x) for x in input().split()]
    
    if collinear(x1, y1, x2, y2, x3, y3):
        print("Not Possible")
    else:
        a=side(x1,y1,x2,y2)
        b=side(x1,y1,x3,y3)
        c=side(x3,y3,x2,y2)
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**(0.5)
        inradius=area/s
        
        den=((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))**(0.5)
        circumradius=(a*b*c)/den
        
        ring=pi*(circumradius**2)-pi*(inradius**2)
        print('{:.2f}'.format(ring))

